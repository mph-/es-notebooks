# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from numpy import linspace, cos, pi


def txline_demo1_plot(f_MHz=1, l_cm=5):

    v = 0.5 * 3e8
    l = l_cm * 0.01
    f = f_MHz * 1e6

    cycles = 5
    T = cycles / f

    t = linspace(0, T, 201)

    v0 = 5 * (1 + cos(2 * pi * f * t)) / 2
    v1 = 5 * (1 + cos(2 * pi * f * (t - l / v))) / 2

    fig, axes = subplots(1, figsize=(8, 4))
    axes.plot(t, v0, label='start')
    axes.plot(t, v1, label='end')
    axes.set_xlabel('Time (ns)')
    axes.set_ylabel('Voltage (V)')
    axes.set_ylim(0, 5.5)
    axes.legend()


def txline_demo1():
    interact(txline_demo1_plot, l_cm=[5, 10, 20, 50],
             f_MHz=[1, 10, 100, 1000], continuous_update=False)
