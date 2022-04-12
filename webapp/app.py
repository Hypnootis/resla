from flask import Flask, render_template, request

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


@app.route('/<cmd>')
def command(cmd=None):
    if cmd == RESET:
        camera_command = "X"
        response = "Resetting ..."
    else:
        # camera_command = cmd[0].upper()
        camera_command = cmd
        response = "Moving {}".format(cmd.capitalize())

    print(camera_command)
    return response, 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(debug=True)
