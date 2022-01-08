from flask import Flask, render_template, request
import time
import threading
import board
from adafruit_motorkit import MotorKit


app = Flask(__name__)

waterWaitTime = [15, 5]

def pump():
    while(True):
        kit = MotorKit()
        kit.motor1.throttle = 1
        time.sleep(waterWaitTime[0]*60)
        kit.motor1.throttle = 0
        time.sleep(waterWaitTime[1]*60)


th = threading.Thread(target=pump)


@app.route('/')
def index():
    return render_template('index.html', time = waterWaitTime)

@app.route('/updateWater')
def updateWarter():
    waterTime = int(request.args['waterTime'])
    waitTime = int(request.args['waitTime'])
    waterWaitTime[0] = waterTime
    waterWaitTime[1] = waitTime
    pump()
    return render_template('updateWater.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')