# Webcam Activity Pinger

📷 A Python-based system to detect camera usage and notify a Flask API server.

This project monitors webcam activity on your local machine and pings an API while the webcam is in use. The server logs activity and provides a simple web interface to display the current status of the camera.

---

## 🚀 Features

- Detects when your webcam is in use
- Sends PATCH requests every few seconds while the webcam is active
- Sends a stop POST request when webcam usage ends
- Logs events on the server
- Displays the latest camera status via a `/status` web page
- Dockerized Flask server for easy deployment

---

## 🧩 Project Structure

```
webcam-activity-pinger/
├── client.py               # Client script to detect camera use
├── server.py               # Flask API server
├── requirements.txt        # Python dependencies for the server
├── .env                    # Configuration (PORT, etc.)
├── Dockerfile              # Docker image for Flask server
├── camera_events.log       # Log of camera activity
├── docker-compose.yml      # To run the server container
└── README.md               # Project documentation
```


## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/BaseMax/webcam-activity-pinger.git
cd webcam-activity-pinger
```

### 2. Configure Environment Variables

Create a `.env` file:

```env
SERVER_PORT=5000
API_URL=http://localhost:5000
CHECK_INTERVAL=10
```

### 3. Run the Flask Server in Docker

```bash
docker-compose up --build
```

Server will be available at: `http://localhost:5000`

### 4. Run the Client (on your host)

```bash
pip install -r requirements.txt
python client.py
```

---

## 🌐 API Endpoints

| Method | Endpoint        | Description             |
|--------|------------------|-------------------------|
| PATCH  | `/camera`       | Mark camera as active   |
| POST   | `/camera/stop`  | Mark camera as stopped  |
| GET    | `/status`       | View current status     |

---

## 🪵 Logging

All camera activity is saved to `camera_events.log`.

---

## 📄 License

MIT License © 2025 [BaseMax](https://github.com/BaseMax)
