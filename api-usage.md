# Azure Custom Vision Prediction API Usage

This document explains how the **Azure Custom Vision Prediction API** is used in the *Classroom Attention Detection* project.

---
Note:
API keys are private and not shared in this repository.

## 📥 Input

The API accepts:
- 📷 **Image file** captured from webcam (JPEG format)
- 🌐 **Image URL** (optional, not used in this project)

In this project, images are captured using **OpenCV** and sent as binary data.

---

## 📤 Output

The API returns a JSON response containing:
- Predicted attention class:
  - `Focused`
  - `Looking_Away`
  - `Sleeping`
- Probability score for each class

### Sample Response
```json
{
  "predictions": [
    { "tagName": "Focused", "probability": 0.82 },
    { "tagName": "Looking_Away", "probability": 0.12 },
    { "tagName": "Sleeping", "probability": 0.06 }
  ]
}


