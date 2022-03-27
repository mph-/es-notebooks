# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import linspace, zeros, nan
from .txline import LosslessTxLine


def txline_receiver_termination_demo1_plot(Z0=60, Rs=20, Vt=0, t_ns=0):

    Rl = Z0

    # Driver voltage.
    Vd = 4.0
    Vmax = Vd * 2

    txline = LosslessTxLine(Z0, Rs, Rl, l=1, v=2 * 3e8 / 3)

    x = linspace(0, 1, 201)

    t = t_ns * 1e-9

    V = txline.Vstep(Vd, x, t, Vt)
    I = txline.Istep(Vd, x, t, Vt)

    fig, axes = subplots(2, 2, figsize=(12, 6))

    axes[0, 0].plot(x, V)
    axes[0, 0].plot(x[0], V[0], 'o', color='C0')
    axes[0, 0].plot(x[-1], V[-1], 'o', color='C2')
    axes[0, 0].grid(True)
    axes[0, 0].set_ylim(0, Vmax)
    # axes[0, 0].set_xlabel('Distance (m)')
    axes[0, 0].set_ylabel('Voltage (V)')

    axes[1, 0].plot(x, I * 1e3, color='C1')
    axes[1, 0].plot(x[0], I[0] * 1e3, 'o', color='C1')
    axes[1, 0].plot(x[-1], I[-1] * 1e3, 'o', color='C3')
    axes[1, 0].grid(True)
    axes[1, 0].set_ylim(-60, 60)
    axes[1, 0].set_xlabel('Distance (m)')
    axes[1, 0].set_ylabel('Current (mA)')

    tv = linspace(0, 40e-9, 201)
    Vs = zeros(len(tv))
    Is = zeros(len(tv))
    Vl = zeros(len(tv))
    Il = zeros(len(tv))

    for m, t1 in enumerate(tv):
        if t1 > t:
            Vs[m] = nan
            Is[m] = nan
            Vl[m] = nan
            Il[m] = nan
        else:
            Vs[m] = txline.Vstep(Vd, 0, t1, Vt)
            Is[m] = txline.Istep(Vd, 0, t1, Vt)
            Vl[m] = txline.Vstep(Vd, 1, t1, Vt)
            Il[m] = txline.Istep(Vd, 1, t1, Vt)

    dt = tv[1] - tv[0]
    m = int(t / dt + 0.5)

    axes[0, 1].plot(tv * 1e9, Vs, label='source')
    axes[0, 1].plot(tv * 1e9, Vl, color='C2', label='load')
    axes[0, 1].plot(t * 1e9, Vs[m], 'o', color='C0')
    axes[0, 1].plot(t * 1e9, Vl[m], 'o', color='C2')
    axes[0, 1].grid(True)
    axes[0, 1].set_ylim(0, Vmax)
    axes[0, 1].set_ylabel('Voltage (V)')
    axes[0, 1].set_xlim(0, 40)
    axes[0, 1].legend()

    axes[1, 1].plot(tv * 1e9, Is * 1e3, color='C1', label='source')
    axes[1, 1].plot(tv * 1e9, Il * 1e3, color='C3', label='load')
    axes[1, 1].plot(t * 1e9, Is[m] * 1e3, 'o', color='C1')
    axes[1, 1].plot(t * 1e9, Il[m] * 1e3, 'o', color='C3')
    axes[1, 1].grid(True)
    axes[1, 1].set_ylim(-60, 60)
    axes[1, 1].set_xlabel('Time (ns)')
    axes[1, 1].set_ylabel('Current (mA)')
    axes[1, 1].set_xlim(0, 40)
    axes[1, 1].legend()

    fig.tight_layout()


def txline_receiver_termination_demo1():
    interact(txline_receiver_termination_demo1_plot, Z0=[50, 60, 80, 100],
             Rs=[0, 10, 20, 30, 40, 50, 60, 80, 100],
             Rl=[0, 10, 20, 30, 40, 50, 60, 80, 100, 1000000],
             Vt=[0, 1, 2, 3, 4, 5],
             t_ns=(0, 40, 1),
             continuous_update=False)
