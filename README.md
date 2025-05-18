# Webcam Activity Pinger 📷

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-1.1.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

Webcam Activity Pinger is a Python-based system designed to detect camera usage and notify a Flask API server. This tool is particularly useful for environments where monitoring camera activity is crucial, such as in meetings or virtual classrooms. By leveraging the power of Python and Flask, this project aims to provide a simple yet effective solution for real-time camera detection.

## Features

- **Real-time Camera Detection**: Monitors webcam activity continuously.
- **Flask API Integration**: Sends notifications to a Flask server when the camera is in use.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **Lightweight and Fast**: Minimal resource usage while running.
- **Customizable Notifications**: Easily modify notification settings to suit your needs.

## Topics

This project covers various topics, including:

- camera
- camera-meeting
- detect-meeting
- flask
- in-meeting
- iot
- meeting
- microphone
- py
- python
- python3
- script
- video

## Installation

To get started with Webcam Activity Pinger, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JayBeatzxiv/webcam-activity-pinger.git
   cd webcam-activity-pinger
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.9 or higher installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and Execute**:
   You can find the latest release [here](https://github.com/JayBeatzxiv/webcam-activity-pinger/releases). Download the necessary files and execute the script.

## Usage

### Starting the Flask Server

Before running the webcam activity detection, you need to start the Flask server. Use the following command:

```bash
python app.py
```

### Running the Webcam Activity Detector

In another terminal window, run the webcam activity detection script:

```bash
python detect_camera.py
```

### Notifications

Once the detection script is running, it will notify the Flask server whenever the camera is in use. You can customize the notification behavior in the `config.py` file.

## Configuration

The configuration file allows you to set various parameters:

- **API_URL**: URL of the Flask server.
- **NOTIFICATION_TYPE**: Type of notification (e.g., email, SMS).
- **CHECK_INTERVAL**: Time interval to check for camera activity (in seconds).

Example `config.py`:

```python
API_URL = "http://localhost:5000/notify"
NOTIFICATION_TYPE = "email"
CHECK_INTERVAL = 5
```

## Testing

You can test the system by simulating camera activity. Simply run the detection script and then open any application that uses the webcam, such as Zoom or Skype. The Flask server should receive notifications indicating that the camera is active.

## Troubleshooting

If you encounter issues, consider the following:

- Ensure that your webcam drivers are installed and functioning.
- Check that the Flask server is running before executing the detection script.
- Review the logs for any error messages.

## Contribution

We welcome contributions to improve Webcam Activity Pinger. If you have suggestions or enhancements, please fork the repository and submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask community for their excellent framework.
- Special thanks to the contributors who have made this project better.

## Further Reading

For more information about Flask and webcam detection, consider checking out these resources:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV for Python](https://opencv-python-tutroals.readthedocs.io/en/latest/)
- [Python Webcam Access](https://www.geeksforgeeks.org/accessing-webcam-using-python/)

## Links

For the latest releases, please visit [here](https://github.com/JayBeatzxiv/webcam-activity-pinger/releases).

## Contact

For any inquiries or support, feel free to reach out via GitHub issues or contact the repository owner directly.

---

Thank you for using Webcam Activity Pinger!