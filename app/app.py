from __future__ import absolute_import

import os
import serial
import time

# from LMP import sensor_reading

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app)

port = "/dev/cu.usbmodem1411"
baudrate = 9600
# angle = [0, 90, 45, -45, "LCP", "RCP"]
ser = serial.Serial(port, baudrate)

@app.route('/')
def hello_world():
  return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def file_upload():

    print request

    if 'file' not in request.files:
        print 'No file part'
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print 'No selected file'
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print 'File Upload Successful'
        return redirect('/')


@app.route('/lightsensor')
def get_reading():
    # sensor_reading()

    time.sleep(2)

    ser.flush()
    ser.write('3')

    time.sleep(1)

    measurement = ser.readline()

    return measurement


@app.route('/motor', methods=['POST'])
def motor():
    data = request.get_json()
    direction = data.get('dir')

    time.sleep(2)
    ser.flush()

    if direction == 'left':
        ser.write('4')
    if direction == 'right':
        ser.write('5')
    # ser.write('4')
    time.sleep(1)

    return 'successful'

# @socketio.on('sensor reading', namespace='/test')
# def sensor_reading():
#     num = 0
#     while True:
#         num = num + 1
#         socketio.emit('reading', {'num': num}, namespace='/test')

@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
  # socketio.run(app)
