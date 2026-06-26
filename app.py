from flask import Flask, render_template
from feelings_data import feelings

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", feelings=feelings)

if __name__ == "__main__":
    app.run(debug=True)