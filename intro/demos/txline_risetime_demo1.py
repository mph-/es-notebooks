# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from numpy import linspace, cos, pi
from .txline import LosslessTxLine


def step(t):
    return (t >= 0) * 1


def rampstep(t, Tr):

    t = (t / Tr)
    return t * (t < 1) * (t >= 0) + (t >= 1)


def txline_risetime_demo1_plot(Tr_ns=1, l_cm=5):

    # Allow for 10% to 90%
    Tr = Tr_ns / 0.8 * 1e-9

    txline = LosslessTxLine(60, 20, 60, l=l_cm * 1e-2, v=2 * 3e8 / 3)
    T = txline.T

    t = linspace(0, Tr_ns * 1e-9 * 5, 201)

    vs = 4 * rampstep(t, Tr)
    vl = 4 * rampstep(t - T, Tr)

    if txline.l > txline.v * Tr / 6:
        linestyle = 'solid'
    else:
        linestyle = 'dashed'

    fig, axes = subplots(1, figsize=(8, 4))
    axes.plot(t * 1e9, vs, label='start')
    axes.plot(t * 1e9, vl, label='end', linestyle=linestyle)
    axes.set_xlabel('Time (ns)')
    axes.set_ylabel('Voltage (V)')
    axes.set_ylim(0, 5.5)
    axes.legend()


def txline_risetime_demo1():
    interact(txline_risetime_demo1_plot, l_cm=[5, 10, 20, 50, 100],
             Tr_ns=[1, 2, 10, 100, 1000], continuous_update=False)
