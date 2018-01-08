"""
Assignment: 6.3
The input forms for the parameters for the CO2
and temperature plots are generated using wtforms
in this module.

Author: kevinjc
"""

from wtforms import Form, FloatField, validators

class Co2Form(Form):
    """ Input form for the CO2 plot """
    tmin = FloatField(
        label='Time min', default=1750,
        validators=[validators.InputRequired()])
    tmax = FloatField(
        label='Time max', default=2015,
        validators=[validators.InputRequired()])
    co2Min = FloatField(
        label='CO2 min', default=0,
        validators=[validators.InputRequired()])
    co2Max = FloatField(
        label='CO2 max', default=10000,
        validators=[validators.InputRequired()])

class TemperatureForm(Form):
    """ Input form for the temperature plot """
    tmin = FloatField(
        label='Time min', default=1815,
        validators=[validators.InputRequired()])
    tmax = FloatField(
        label='Time max', default=2016,
        validators=[validators.InputRequired()])
    tempMin = FloatField(
        label='temperature max', default=-10,
        validators=[validators.InputRequired()])
    tempMax = FloatField(
        label='temperature min', default=10,
        validators=[validators.InputRequired()])
    m = FloatField(
        label='Month', default=1,
        validators=[validators.InputRequired()])
