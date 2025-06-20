# 🔊 Volume Control Using Hand Gesture

Control your system's audio volume using just your hand gestures via webcam! This Python project utilizes real-time hand tracking with OpenCV and MediaPipe to dynamically adjust the volume based on the distance between your thumb and index finger.

## 📽️ Demo
https://github.com/Peehuagrawal/handtracking/assets/86126709/c4e9b4c5-e3c1-4b2b-9c2b-67cc67911939

## 📌 Features

- Real-time hand tracking using webcam
- Detects hand landmarks using MediaPipe
- Calculates distance between fingers to set volume level
- Visual feedback via overlay on video feed
- Modular code using `HandTrackingModule.py`

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyCaw (for volume control)
- NumPy
- Math

## 📂 Project Structure

```
handtracking/
│
├── HandTrackingModule.py   # Custom module for hand detection
├── VolumeControl.py        # Main script for volume control
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Peehuagrawal/handtracking.git
cd handtracking
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. Then install required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Project

```bash
python VolumeControl.py
```

Make sure your webcam is enabled and your system allows access.

## 🔮 Future Improvements

- Add support for more gestures (e.g., play/pause, skip)
- Optimize for low-light conditions
- Implement GUI for better user control
- Deploy as a lightweight desktop app

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙋‍♀️ Author

**Peehu Agrawal**  
🔗 [GitHub](https://github.com/Peehuagrawal)
