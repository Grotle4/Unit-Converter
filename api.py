from flask import Flask, render_template, request
import converter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("length_page.html")

@app.route("/length")
def length():
    return render_template("length_page.html")

@app.route("/weight")
def weight():
    return render_template("weight_page.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature_page.html")




@app.route("/convert", methods=["POST", "GET"]) #TODO: Change to POST in HTML and get values from input name attributes, also work on converter script
def check_convert():
    unit = request.form.get("unit")
    unit_from = request.form.get("unit_from")
    unit_to = request.form.get("unit_to")
    page_type = request.form.get("page")
    converted = converter.conversion(unit, unit_from, unit_to, page_type)
    return render_template("convert_page.html", unit = unit, unit_from = unit_from, unit_to = unit_to, page = page_type, converted= converted)




if __name__ == "__main__":
    app.run(debug=True)