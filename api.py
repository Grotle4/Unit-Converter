from flask import Flask, render_template, request
import converter
import get_unit_suffix

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
    suffix = get_unit_suffix.get_suffix(converted, unit_to, page_type)
    return render_template("convert_page.html", suffix= suffix, converted= converted, page_type= page_type)


@app.route("/return", methods=["POST"])
def go_to_home():
    page_type = request.form.get("page")
    print(page_type)
    print(type(page_type))

    return render_template(f"{page_type}_page.html")


if __name__ == "__main__":
    app.run(debug=True)