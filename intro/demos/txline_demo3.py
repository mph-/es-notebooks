# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import linspace
from .txline import LosslessTxLine


def txline_demo3_plot(Z0=60, Rs=20, Rl=1e6, t_ns=0):

    # Driver voltage.
    Vd = 4.0

    txline = LosslessTxLine(Z0, Rs, Rl, l=1, v=2 * 3e8 / 3)

    x = linspace(0, 1, 201)

    t = t_ns * 1e-9

    V = txline.Vstep(Vd, x, t)
    I = txline.Istep(Vd, x, t)

    fig, axes = subplots(2, figsize=(12, 4))

    axes[0].plot(x, V)
    axes[0].grid(True)
    axes[0].set_ylim(0, 7)
    # axes[0].set_xlabel('Distance (m)')
    axes[0].set_ylabel('Voltage (V)')
    axes[0].set_title('$\Gamma_l = %s, \Gamma_s = %s$' %
                      (round(txline.GammaVl, 3), round(txline.GammaVs, 3)))

    axes[1].plot(x, I * 1e3, color='C1')
    axes[1].grid(True)
    axes[1].set_ylim(-100, 100)
    axes[1].set_xlabel('Distance (m)')
    axes[1].set_ylabel('Current (mA)')


def txline_demo3():
    interact(txline_demo3_plot, Z0=[50, 60, 80, 100],
             Rs=[0, 10, 20, 30, 40, 50, 60, 80, 100],
             Rl=[0, 10, 20, 30, 40, 50, 60, 80, 100, 1000000],
             t_ns=(0, 40, 1),
             continuous_update=False)
