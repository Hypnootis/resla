from flask import Flask, render_template, request
import test_servo

app = Flask(__name__, template_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control_servo", methods=["POST"])
def control_servo():
    test_servo.move_wheels()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
