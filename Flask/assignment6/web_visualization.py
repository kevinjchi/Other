"""
Assignment 6.2 and 6.3
Interactive web visualization of the temperature and CO2 plots.

Author: kevinjc
"""

import sys
from model import Co2Form, TemperatureForm
from flask import Flask, render_template, request
from plot_temp_CO2 import plot_temperature, plot_CO2

app = Flask(__name__)

try:
    template_name = sys.argv[1]
except IndexError:
    template_name = "view"

# routes to
@app.route("/")
def index():
    """ Renders the homepage """
    return render_template("index.html")

@app.route("/plot_co2", methods=["GET", "POST"])
def co2_plot_route():
    """ Renders the CO2 plot """
    form = Co2Form(request.form)

    if request.method == "POST" and form.validate():
        result = plot_CO2(form.tmin.data, form.tmax.data,
                          form.co2Min.data, form.co2Max.data)
    else:
        result = None

    print_debug_info(form)

    return render_template(template_name + '.html', form=form, result=result)

@app.route("/plot_temperature", methods=["GET", "POST"])
def temperature_plot_route():
    """ Renders the temperature plot """
    form = TemperatureForm(request.form)

    if request.method == "POST" and form.validate():
        result = plot_temperature(form.tmin.data, form.tmax.data,
                                  form.tempMin.data, form.tempMax.data,
                                  form.m.data)
    else:
        result = None

    print_debug_info(form)

    return render_template(template_name + '.html', form=form, result=result)

def print_debug_info(form):
    """ Prints additional debugging info if the app is in debug mode """
    if app.debug:
        print(form, dir(form))

        for field in form:
            print(field.name)


#Running on http://localhost:5000/
if __name__ == "__main__":
    app.debug = True
    app.run()
