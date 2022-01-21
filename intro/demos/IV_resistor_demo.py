# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from numpy import linspace

def IV_resistor_demo_plot(R=50):

    Voh = linspace(0, 5, 200)
    Ioh = -Voh / R

    fig, ax = subplots(1)
    ax.plot(Voh, Ioh * 1e3, color='blue')
    ax.set_ylim(-250, 250)
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (mA)')
    ax.grid(True)

def IV_resistor_demo():
    interact(IV_resistor_demo_plot,
             R=(10, 100, 10),
             continuous_update=False)
