import os
import cv2
from flask import render_template, url_for, Blueprint, Response

main = Blueprint('main', __name__)

# URL for phone camera
url = "http://192.168.0.104:4747/video"
# recommended app for phone DroidCam linked through local Network both pc and mobile
camera = cv2.VideoCapture(url) # if laptop cam then use 0 

# Getting the absolute path to the Haarcascade directory
base_dir = os.path.abspath(os.path.dirname(__file__))

# loading Haarcascade classifiers with absolute paths
detector = cv2.CascadeClassifier(os.path.join(base_dir, 'haarcascade_frontalface_default.xml'))
eye_detector = cv2.CascadeClassifier(os.path.join(base_dir, 'haarcascade_eye.xml'))
cat_face = cv2.CascadeClassifier(os.path.join(base_dir, 'haarcascade_frontalcatface_extended.xml'))
smile = cv2.CascadeClassifier(os.path.join(base_dir, 'haarcascade_smile.xml'))

# checking if the classifiers are loaded correctly
if detector.empty():
    raise Exception("Failed to load face detector Haarcascade file.")
if eye_detector.empty():
    raise Exception("Failed to load eye detector Haarcascade file.")
if cat_face.empty():
    raise Exception("Failed to load cat face detector Haarcascade file.")
if smile.empty():
    raise Exception("Failed to load smile detector Haarcascade file.")

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detecting human faces
            faces = detector.detectMultiScale(gray, 1.1, 7)
            # Detecting cat faces
            cat_faces = cat_face.detectMultiScale(gray, 1.1, 5)

            # Loop over detected human faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # Detecting eyes in the face region
                eyes = eye_detector.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Green rectangle for eyes

                # Detecting smiles in the face region
                smiles = smile.detectMultiScale(roi_gray, 1.8, 20)
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 0), 2)  # Black rectangle for smiles

            # Loop over detected cat faces
            for (cx, cy, cw, ch) in cat_faces:
                cv2.rectangle(frame, (cx, cy), (cx + cw, cy + ch), (0, 165, 255), 2)  # Orange rectangle for cat faces

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/Video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
