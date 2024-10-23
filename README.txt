Real-Time Detection Using Flask and OpenCV(Haarcascade)

Project Summary
This project is a real-time video stream detection application built using Flask and OpenCV. The application captures video from a phone camera or laptop webcam and processes it using pre-trained Haarcascade classifiers. It detects human faces, eyes, smiles, and cat faces in the video feed. The processed video stream, with detection overlays, is then rendered in a simple web interface. The application is lightweight, runs on local devices, and is intended for live video processing through a web browser.

Project Goal
The primary goal of this project is to demonstrate how to use OpenCV’s Haarcascade classifiers for real-time object detection in video streams and to integrate this functionality into a web application using Flask. This project can serve as a foundation for further development into more complex computer vision applications like security monitoring, facial recognition, or custom object detection models.

Key objectives:

Real-time face, eye, smile, and cat face detection from video streams.
Integration of OpenCV with Flask for serving live video to a web interface.
Demonstrating the use of Haarcascade classifiers for object detection.
Providing an easy-to-use template for deploying computer vision applications on the web.

How to Run the Application

Prerequisites
Make sure you have the following installed:
Python 3.x
Flask
OpenCV
A camera (phone or laptop)

Steps to Set Up and Run

Clone the repository: Clone the repository to your local machine

Set up a virtual environment (optional but recommended): Create and activate a virtual environment

pip install Flask opencv-python

Configure the video source:
Phone Camera: If you are using a phone camera, download the DroidCam app on your phone and make sure both the phone and computer are connected to the same network. Modify the url variable in main.py to reflect your DroidCam's streaming URL (e.g., http://192.168.x.x:4747/video).
Laptop Camera: If using your laptop webcam, modify the camera variable in main.py to 0.

Run the application: Run the Flask application using the command below:

export FLASK_APP=your_project_folder_name
flask run
This will start the development server on http://127.0.0.1:5000/

You should now see the live video stream with real-time object detection (faces, eyes, smiles, and cat faces).

![My Image](https://github.com/THOTHSM/Real-Time-Detection-Using-Flask-and-OpenCV-Haarcascade-/blob/main/sceenshot.png?raw=true)
