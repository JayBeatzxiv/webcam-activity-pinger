import cv2
import time
import requests
import os
import threading
import sys
import select
import platform
from typing import Optional
from dotenv import load_dotenv

if platform.system() == "Windows":
    import msvcrt
else:
    import termios
    import tty

load_dotenv()

API_URL: str = os.getenv("API_URL", "http://localhost:5000")
CHECK_INTERVAL: int = int(os.getenv("CHECK_INTERVAL", 10))
CAMERA_MODE: str = os.getenv("CAMERA_CAMERA_MODE", "all").lower()
MAX_CAMERAS: int = int(os.getenv("MAX_CAMERAS", 3))

stop_flag: bool = False

def debug_camera_scan():
    for idx in range(MAX_CAMERAS):
        try:
            cap = cv2.VideoCapture(idx)
            if cap.isOpened():
                backend = cap.getBackendName() if hasattr(cap, 'getBackendName') else "unknown"
                print(f"Index {idx}: opened=True, backend={backend}")
            else:
                print(f"Index {idx}: opened=False")
            cap.release()
        except Exception as e:
            print(f"Index {idx}: error={e}")

def is_camera_in_use() -> bool:
    if CAMERA_MODE in {"front", "0"}:
        indices = [0]
    elif CAMERA_MODE in {"back", "1"}:
        indices = [1]
    elif "," in CAMERA_MODE:
        indices = [int(i) for i in CAMERA_MODE.split(",") if i.strip().isdigit()]
    else:
        indices = list(range(MAX_CAMERAS))

    backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_V4L2]

    for idx in indices:
        for backend in backends:
            cap = cv2.VideoCapture(idx, backend)
            if not cap.isOpened():
                cap.release()
                continue

            fail_count = 0
            for _ in range(3):
                ret, _ = cap.read()
                if not ret:
                    fail_count += 1
                time.sleep(0.1)

            cap.release()

            if fail_count == 3:
                continue
            else:
                return False

    return True

def safe_post(url: str) -> None:
    try:
        requests.post(url, timeout=3)
    except requests.RequestException:
        print("[WARN] Failed to POST to API. Is server running?")

def safe_patch(url: str) -> None:
    try:
        requests.patch(url, timeout=3)
    except requests.RequestException:
        print("[WARN] Failed to PATCH to API. Is server running?")

def check_keypress() -> None:
    global stop_flag
    if platform.system() == "Windows":
        while not stop_flag:
            if msvcrt.kbhit():
                print("[EXIT] Key pressed, exiting...")
                stop_flag = True
                break
            time.sleep(0.1)
    else:
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            while not stop_flag:
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    print("[EXIT] Key pressed, exiting...")
                    stop_flag = True
                    break
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def main() -> None:
    global stop_flag
    was_using_camera: bool = False

    key_thread: threading.Thread = threading.Thread(target=check_keypress)
    key_thread.daemon = True
    key_thread.start()

    try:
        while not stop_flag:
            debug_camera_scan()
            camera_in_use: bool = is_camera_in_use()
            print(camera_in_use, was_using_camera)

            if camera_in_use and not was_using_camera:
                print("[INFO] Camera started")
                safe_patch(f"{API_URL}/camera")
                was_using_camera = True

            elif camera_in_use and was_using_camera:
                print("[INFO] Camera still in use")
                safe_patch(f"{API_URL}/camera")

            elif not camera_in_use and was_using_camera:
                print("[INFO] Camera stopped")
                safe_post(f"{API_URL}/camera/stop")
                was_using_camera = False

            for _ in range(CHECK_INTERVAL):
                if stop_flag:
                    break
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n[EXIT] Interrupted by Ctrl+C")
        stop_flag = True

    finally:
        if was_using_camera:
            safe_post(f"{API_URL}/camera/stop")
        print("[INFO] Exiting cleanly.")

if __name__ == '__main__':
    main()
