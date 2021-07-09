from utils import generator
from services.Camera import VideoStreamGet
from services.FaceDetector import FaceDetector
from flask import Flask, Response

app = Flask(__name__)


@app.route('/video_feed')
def video_feed():
    detector = FaceDetector('../weights/yolov5n-face.pt')
    camera = VideoStreamGet(
        src='rtsp://admin:1@192.168.1.168:554/mode=real&idc=1&ids=1').start()
    return Response(generator.frame(camera, detector), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
