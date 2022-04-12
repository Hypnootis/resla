from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

servoPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)


def turn_right():
    p.start(0)
    try:
        p.ChangeDutyCycle(2.5)
        print("Turning wheels right")
        time.sleep(0.5)
    except:
        print("Whoops, error with the controls")


def turn_left():
    p.start(0)
    try:
        p.ChangeDutyCycle(10)
        print("Turning wheels left")
        time.sleep(0.5)
    except:
        print("Whoops, error with the controls")


def reset_wheels():
    p.start(0)
    try:
        p.ChangeDutyCycle(7.5)
        print("Straightening wheels")
        time.sleep(1.5)
    except:
        print("Whoops, error with the controls")


app = Flask(__name__, template_folder="templates")
LEFT, RIGHT, UP, DOWN, RESET = "left", "right", 'up', 'down', 'reset'
AVAILABLE_COMMANDS = {
    "Left": LEFT,
    "Right": RIGHT,
    "Up": UP,
    "Down": DOWN,
    "Reset": RESET
}


@app.route('/')
def execute():
    return render_template("main.html", commands=AVAILABLE_COMMANDS)


# @app.route('/<cmd>')
# def command(cmd=None):
#     if cmd == RESET:
#         camera_command = "X"
#         response = "Resetting ..."
#     else:
#         # camera_command = cmd[0].upper()
#         camera_command = cmd
#         response = "Moving {}".format(cmd.capitalize())
#
#     print(camera_command)
#     return response, 200, {'Content-Type': 'text/plain'}

@app.route('/<cmd>')
def command(cmd=None):
    if cmd == RESET:
        camera_command = "X"
        response = "Resetting ..."
        reset_wheels()
    else:
        camera_command = cmd[0].upper()
        camera_command = cmd
        response = "Moving {}".format(cmd.capitalize())
    #if camera_command == RESET:
    #    reset_wheels()
    #    response = "Moving {}".format(cmd.capitalize())
    if camera_command == LEFT:
        turn_left()
        response = "Moving {}".format(cmd.capitalize())
    elif camera_command == RIGHT:
        turn_right()
        response = "Moving {}".format(cmd.capitalize())
    return response, 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(debug=True)
