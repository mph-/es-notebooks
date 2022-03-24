# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import zeros, arange
from .txreflect import txreflect


def txline_demo2_plot(Z0=60, ZD=40, ZL=1e6):

    # Driver voltage.
    Vs = 4.0

    # Delay along transmission line (samples).
    T = 100

    # Duration of experiment (samples).
    N = 2000

    t = arange(N) / T - 1
    m = (t >= 0)

    # Driving voltage.
    Vd = zeros(N)
    Vd[m] = Vs

    [VD, VL] = txreflect(ZD, ZL, Z0, T, Vd)

    # Plot time in terms of delays along transmission line.
    # Offset time origin by one transmission line delay.

    m = t < 10

    fig, axes = subplots(3, figsize=(8, 4))

    fig.tight_layout()

    axes[0].plot(t[m], Vd[m])
    axes[0].grid(True)
    axes[0].set_ylim(0, 7)
    axes[0].set_title('Driver voltage')
    axes[0].set_xticks([0, 2, 4, 6, 8, 10])
    axes[0].set_xticklabels(['0', '2T', '4T', '6T', '8T', '10T'])
    axes[0].set_yticks([0, 2, 4, 6])

    axes[1].plot(t[m], VD[m])
    axes[1].grid(True)
    axes[1].set_ylim(0, 7)
    axes[1].set_title('Source voltage')
    axes[1].set_xticks([0, 2, 4, 6, 8, 10])
    axes[1].set_xticklabels(['0', '2T', '4T', '6T', '8T', '10T'])
    axes[1].set_yticks([0, 2, 4, 6])

    axes[2].plot(t[m], VL[m])
    axes[2].grid(True)
    axes[2].set_ylim(0, 7)
    axes[2].set_title('Load voltage')
    axes[2].set_xticks([0, 2, 4, 6, 8, 10])
    axes[2].set_xticklabels(['0', '2T', '4T', '6T', '8T', '10T'])
    axes[2].set_yticks([0, 2, 4, 6])
    axes[2].set_xlabel('Time')


def txline_demo2():
    interact(txline_demo2_plot, Z0=[50, 60, 80, 100],
             ZD=[0, 10, 20, 30, 40, 50, 60, 80, 100],
             ZL=[0, 10, 20, 30, 40, 50, 60, 80, 100, 1e6],
             continuous_update=False)
