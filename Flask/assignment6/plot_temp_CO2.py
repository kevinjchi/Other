"""
Assignment 6.1
Plots for CO2 over time and temperature over time

Author: kevinjc
"""

import os
import time
import glob
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


#co2_stats = pd.read_csv("./co2.csv")
#temp_stats = pd.read_csv("./temperature.csv")

#print(temp_stats.head())

def plot_temperature(time_min=None, time_max=None, temp_min=None, temp_max=None, month=None):
    """
    Function to plot time vs temperature.
    Parameters to adjust the x-axis: time_min, time_max
    to adjust the y-axis: temp_min, temp_max
    to adjust what month to plot: month - insert 1,2,3...,12.
    If no parameters are inputed, the values for January is plotted.
    """

    # If no month is inserted, plots the temperature for January
    if month is None:
        month = 1
    month = int(month)

    temp_stats = pd.read_csv("./data/temperature.csv")
    # renaming the columns in order to make it easier to input
    temp_stats = temp_stats.rename(
        columns={'January': 1, 'February': 2,
                 'March': 3, 'April': 4,
                 'May': 5, 'June': 6,
                 'July': 7, 'August': 8,
                 'September': 9, 'October': 10,
                 'November': 11, 'December': 12})
    plt.figure()
    plt.plot(temp_stats["Year"], temp_stats[month], '-b')

    # labels
    plt.ylabel(r"Temperature [$^\circ C$]")
    plt.xlabel("Time [Year]")

    # limits
    plt.ylim(temp_min, temp_max)
    plt.xlim(time_min, time_max)
    plt.title("Month:{}".format(month))

    # Clean up the static folder
    delete_plots()

    # make a unique filename that the browser has not cached
    plotfile = os.path.join("static", str(time.time()) + ".png")
    plt.savefig(plotfile)

    return plotfile

def plot_CO2(time_min=None, time_max=None, co2_min=None, co2_max=None):
    """
    Function to plot time vs CO2 level.
    Parameters to adjust the x-axis: time_min, time_max
    and to adjust the y-axis: co2_min, co2_max
    If no parameters are inserted, the whole datasett is plotted.
    """
    co2_stats = pd.read_csv("./data/co2.csv")
    plt.figure()
    plt.plot(co2_stats["Year"], co2_stats["Carbon"], '-r')

    #labels
    plt.ylabel("$CO_2$ [million metric tons]")
    plt.xlabel("Time [Year]")

    #limits
    plt.ylim(co2_min, co2_max)
    plt.xlim(time_min, time_max)

    # Clean up the static folder
    delete_plots()

    #make a unique filename that the browser has not cached
    plotfile = os.path.join("static", str(time.time()) + ".png")
    plt.savefig(plotfile)

    return plotfile

def delete_plots():
    """ Cleans up the static folder by deleting all plots """
    if not os.path.isdir("static"):
        os.mkdir("static")
    else:
        #remove old plot files
        for filename in glob.glob(os.path.join("static", "*.png")):
            os.remove(filename)

if __name__ == "__main__":
    print(plot_CO2)
    print(plot_temperature)
