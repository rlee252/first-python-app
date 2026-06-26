from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/feelings.json", "r") as file:
    feelings = json.load(file)


@app.route("/")
def home():
    return render_template("index.html", feelings=feelings)


if __name__ == "__main__":
    app.run(debug=True)