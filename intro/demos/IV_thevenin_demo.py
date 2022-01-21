# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from numpy import linspace

def IV_thevenin_demo_plot(R=50, Vdd=5):

    Voh = linspace(0, 5, 200)
    Ioh = (Vdd - Voh) / R

    fig, ax = subplots(1)
    ax.plot(Voh, Ioh * 1e3, color='red')
    ax.set_ylim(0, 250)
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (mA)')
    ax.grid(True)

def IV_thevenin_demo():
    interact(IV_thevenin_demo_plot,
             R=(10, 100, 10),
             Vdd=(1, 5, 1),
             continuous_update=False)
