import streamlit as st
import cv2
import requests
import tempfile
import time
import csv
from datetime import datetime

# -------------------------------
# 🔑 AZURE CONFIG
# -------------------------------
PREDICTION_URL = "AZURE_PREDICTION_URL"
PREDICTION_KEY = "AZURE_PREDICTION_KEY"

HEADERS = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/octet-stream"
}

# -------------------------------
# 🎨 UI SETUP
# -------------------------------
st.set_page_config("Class Attention App", layout="centered")
st.title("📊 Class Attention")
st.subheader("Attention Level")

# Initialize session state
if "last_result" not in st.session_state:
    st.session_state.last_result = None

# -------------------------------
# 📸 TEST ATTENTION
# -------------------------------
if st.button("📷 Test Attention"):

    st.info("Camera started... capturing image")

    cam = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cam.read()
    cam.release()
    cv2.destroyAllWindows()

    if not ret:
        st.error("❌ Camera capture failed")
    else:
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        cv2.imwrite(temp.name, frame)
        st.success("✅ Image captured")

        with open(temp.name, "rb") as img:
            response = requests.post(
                PREDICTION_URL,
                headers=HEADERS,
                data=img
            )

        if response.status_code != 200:
            st.error("❌ Azure error")
            st.text(response.text)
        else:
            result = response.json()
            best = max(result["predictions"], key=lambda x: x["probability"])

            tag = best["tagName"]
            prob = round(best["probability"] * 100, 2)

            st.session_state.last_result = (tag, prob)

            if tag == "Focused":
                st.success(f"🟢 Focused ({prob}%)")
            elif tag == "Looking_Away":
                st.warning(f"🟡 Looking Away ({prob}%)")
            else:
                st.error(f"🔴 Sleeping ({prob}%)")

# -------------------------------
# 📝 MARK ATTENDANCE
# -------------------------------
if st.button("📝 Mark Attendance"):

    if st.session_state.last_result is None:
        st.warning("⚠️ Please test attention first")
    else:
        tag, prob = st.session_state.last_result
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([time_now, tag, prob])

        st.success("✅ Attendance marked successfully")

# -------------------------------
# 👤 STUDENT PROFILE (WORKING)
# -------------------------------
st.divider()
st.subheader("👤 Student Profile")

with st.form("student_profile_form"):

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    branch = st.text_input("Branch")
    year = st.selectbox("Year", ["1st", "2nd", "3rd", "4th"])

    submit_profile = st.form_submit_button("💾 Save Profile")

    if submit_profile:
        if name == "" or roll == "" or branch == "":
            st.warning("⚠️ Please fill all fields")
        else:
            with open("students.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([roll, name, branch, year])

            st.success("✅ Student profile saved successfully")


# -------------------------------
# ❌ EXIT
# -------------------------------
if st.button("❌ Exit"):
    st.warning("App stopped. Close browser tab.")
