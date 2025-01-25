from flask import Flask, render_template, request
import ai
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        ask = request.form["description"]

        url = ai.imagecreate(ask)

        return render_template("index.html", image=url)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
