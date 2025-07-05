# NexaGesture
# ✋ NexaGesture: Gesture-Based System Control using Computer Vision

NexaGesture is a Python-based computer vision project that enables **gesture control** to adjust **system brightness** and **volume** using real-time hand tracking through a webcam.

This project uses **Mediapipe** for hand detection, **OpenCV** for video processing, **Pycaw** for volume control, and **screen-brightness-control** for screen brightness adjustment.

---

## 🚀 Features
- 👋 Real-time hand gesture detection
- 🔆 Control system brightness using **left hand** gestures
- 🔊 Control system volume using **right hand** gestures
- 💻 Smooth, responsive system control
- 🎥 Webcam-based tracking
- 📊 Visual feedback on the screen (current brightness and volume)

---

## 📂 Folder Structure
```plaintext
NEXAGESTURE PROJECT/
│
├── main.py                  # Main application file
├── hand_detector.py         # Handles hand detection using Mediapipe
├── gesture_controller.py    # Processes gestures and applies system controls
├── utils.py                 # Utility functions (if needed)
├── __pycache__/             # Python cache files (auto-generated)        
└── README.md                # Project documentation

```
🛠️ Tech Stack
```
Python 3.11+

OpenCV - Real-time image processing

Mediapipe - Hand tracking model

Numpy - Numerical calculations

Pycaw - Windows volume control API

Screen Brightness Control - Cross-platform brightness management

Comtypes - Windows COM interface interaction

```
🔧 Setup Instructions

1. Clone the Repository
  ```
   git clone https://github.com/singhshrasti/NexaGesture-project.git
cd NexaGesture-project

```
3. Create Virtual Environment (Optional but Recommended)
   ```
   python -m venv venv
   venv\Scripts\activate

   ```
5. Install Dependencies
   ```

   pip install opencv-python mediapipe numpy pycaw screen-brightness-control comtypes

   ```

7. Run the Project
   ```
   python main.py

🎮 How to Use

1.Left Hand Gesture: Control brightness by changing the distance between thumb and index finger.

2.Right Hand Gesture: Control volume by changing the distance between thumb and index finger.

3.Press 'q' to exit the application.

8.📌 Known Issues

Works only on Windows (because of Pycaw and system brightness library support).

Requires a good quality webcam for accurate gesture detection.




