from flask import render_template, request, redirect, url_for, jsonify
from app import app
from .equation_plotter import plot_func
from .integration import integrate
from .stofunc import string_to_function

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/equation", methods=["GET"])
def equation_form():
    return render_template("equation.html")

# POST: Handle the form submission
@app.route("/equation", methods=["POST"])
def solve():
    f = request.form.get("equation")
    xmin = request.form.get("xmin")
    xmax = request.form.get("xmax")
    
    return redirect(url_for("result", f=f, xmin=xmin, xmax=xmax))
    
@app.route("/result", methods=["GET"])
def result():
    equation = request.args.get("f")
    xmin = request.args.get("xmin")
    xmax = request.args.get("xmax")
    area = integrate(string_to_function(equation), float(xmin), float(xmax))
    image_path = plot_func(string_to_function(equation), float(xmin), float(xmax))
    # print(image_path)

    # Render the result template with the received data
    return render_template(
        "result.html",
        equation=equation,
        xmin=xmin,
        xmax=xmax,
        area=area
    )
