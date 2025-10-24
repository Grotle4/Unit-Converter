from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("length_page.html")

@app.route("/convert")
def check_convert():
    return "this is a test"


if __name__ == "__main__":
    app.run(debug=True)