from flask import Flask, render_template, request
#import RPi.GPIO as GPIO
from time import sleep

servo_pin = 19

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servo_pin, GPIO.OUT)

#p = GPIO.PWM(servo_pin, 50)

#p.start(0)

app = Flask(__name__, template_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
