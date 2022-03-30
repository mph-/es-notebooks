# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import linspace, zeros, nan
from .txline import LosslessTxLine


def txline_receiver_termination_demo1_plot(Rt=100000, Vt=2, t_ns=0):

    Z0 = 60
    Rs = 20
    Vt = 2

    # Driver voltage.
    Vd = 4.0
    Vmax = Vd * 2

    txline = LosslessTxLine(Z0, Rs, Rt, l=1, v=2 * 3e8 / 3)

    x = linspace(0, 1, 201)

    t = t_ns * 1e-9

    V = txline.Vstep(Vd, x, t, Vt)

    fig, axes = subplots(1, 2, figsize=(12, 6))

    axes[0].plot(x, V)
    axes[0].plot(x[0], V[0], 'o', color='C0')
    axes[0].plot(x[-1], V[-1], 'o', color='C2')
    axes[0].grid(True)
    axes[0].set_ylim(0, Vmax)
    axes[0].set_xlabel('Distance (m)')
    axes[0].set_ylabel('Voltage (V)')

    tv = linspace(0, 40e-9, 201)
    Vs = zeros(len(tv))
    Vl = zeros(len(tv))

    for m, t1 in enumerate(tv):
        if t1 > t:
            Vs[m] = nan
            Vl[m] = nan
        else:
            Vs[m] = txline.Vstep(Vd, 0, t1, Vt)
            Vl[m] = txline.Vstep(Vd, 1, t1, Vt)

    dt = tv[1] - tv[0]
    m = int(t / dt + 0.5)

    axes[1].plot(tv * 1e9, Vs, label='source')
    axes[1].plot(tv * 1e9, Vl, color='C2', label='load')
    axes[1].plot(t * 1e9, Vs[m], 'o', color='C0')
    axes[1].plot(t * 1e9, Vl[m], 'o', color='C2')
    axes[1].grid(True)
    axes[1].set_ylim(0, Vmax)
    axes[1].set_ylabel('Voltage (V)')
    axes[1].set_xlim(0, 40)
    axes[1].legend()

    fig.tight_layout()


def txline_receiver_termination_demo1():
    interact(txline_receiver_termination_demo1_plot,
             Rt=[0, 30, 40, 50, 60, 100, 100000],
             Vt=[0, 1, 2, 3, 4, 5],
             t_ns=(0, 40, 1),
             continuous_update=False)
