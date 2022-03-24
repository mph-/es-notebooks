# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import linspace
from .txline import LosslessTxLine


def txline_demo3_plot(Z0=60, Zs=40, Zl=1e6, t=0):

    # Driver voltage.
    Vd = 4.0

    txline = LosslessTxLine(Z0, Zs, Zl, l=1, v=0.5 * 3e8)

    x = linspace(0, 1, 201)

    t = t * txline.T

    V = txline.V(Vd, x, t)

    fig, axes = subplots(1, figsize=(8, 4))

    axes.plot(x, V)
    axes.grid(True)
    axes.set_ylim(0, 7)
    axes.set_xlabel('Distance (m)')
    axes.set_xlabel('Voltage (V)')


def txline_demo3():
    interact(txline_demo3_plot, Z0=[50, 60, 80, 100],
             Zs=[0, 10, 20, 30, 40, 50, 60, 80, 100],
             Zl=[0, 10, 20, 30, 40, 50, 60, 80, 100, 1e6],
             t=(0, 20, 0.2),
             continuous_update=False)
