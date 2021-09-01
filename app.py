from flask import Flask, jsonify
from flask import Flask, render_template, Response
import cv2

camera = cv2.VideoCapture('rtsp://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream')

app = Flask(__name__)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show resul

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Herok"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/hello/<string:name>')
def Home(name):
    return render_template('home.html', name_html=name)

@app.route('/name')
    return"<font color=blue>วรางคณา นุชเกษม</font> <br> เลขที่ 18 ชั้น ม.4/10"

@app.route('/video')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
