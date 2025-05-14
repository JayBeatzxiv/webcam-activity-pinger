import cv2
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:5000")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 10))

# cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_ERROR)

def is_camera_available():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap.release()
        return False
    ret, _ = cap.read()
    cap.release()
    return ret

def is_camera_in_use():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap.release()
        return False
    ret, _ = cap.read()
    cap.release()
    return ret

def main():
    was_using_camera = False

    while True:
        try:
            camera_in_use = is_camera_in_use()

            if camera_in_use and not was_using_camera:
                print("[INFO] Camera started")
                requests.patch(f"{API_URL}/camera")
                was_using_camera = True

            elif camera_in_use and was_using_camera:
                print("[INFO] Camera still in use")
                requests.patch(f"{API_URL}/camera")

            elif not camera_in_use and was_using_camera:
                print("[INFO] Camera stopped")
                requests.post(f"{API_URL}/camera/stop")
                was_using_camera = False

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\n[EXIT] Interrupted by user")
            if was_using_camera:
                requests.post(f"{API_URL}/camera/stop")
            break

if __name__ == '__main__':
    main()
