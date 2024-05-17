from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    msg = "Exercise 1"
    return render_template("index.html", message=msg)


if __name__ == "__main__":
    app.run(debug=True)