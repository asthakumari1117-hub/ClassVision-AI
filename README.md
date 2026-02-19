# 🎯 ClassVision AI
AI-Powered Classroom Attention & Study Monitoring System


classroom_watch_AI
## ⏱️ Study-Time Monitoring (Live Camera Mode)

ClassWatch AI includes a study-purpose live camera feature to monitor
student attention during study sessions.

### How it Works:
- The camera turns ON when the study session starts
- The student studies in front of the camera
- After **5 minutes**, the system automatically captures an image
- The captured image is analyzed using Azure Custom Vision
- The system detects whether the student is:
  - Focused (Studying)
  - Sleeping
  - Looking Away


This feature helps in monitoring continuous student engagement during
self-study or classroom study time.


An AI-powered classroom monitoring system that detects student attention using Azure Custom Vision.
**Implementation File:** `classroom_watch_AI.py



## Features
- 📷 Real-time camera capture
- 🧠 Attention detection (Focused / Looking Away / Sleeping)
- 📝 Automatic attendance marking
- 👤 Student profile management
- ☁️ Azure Custom Vision integration

## Tech Stack
- Python
- Streamlit
- OpenCV
- Azure Custom Vision
- CSV-based data storage

---

## 📸 Application Screenshots

### Class Attention Dashboard
![Class Attention](images/class_attention.png)

### Student Profile Form
![Student Profile](images/student_profile.png)

### Student Profile Saved
![Profile Saved](images/student_profile_saved.png)

### Attendance Marked
![Attendance](images/mark_attendance.png)


## How to Run
```bash
pip install streamlit opencv-python requests
streamlit run app.py
