# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from numpy import array
from .txline import LosslessTxLine


def txline_lattice_demo1_plot(Z0=60, Rs=20, Rl=1e6, t_ns=0):

    # Driver voltage.
    Vd = 4.0

    txline = LosslessTxLine(Z0, Rs, Rl, l=1, v=2 * 3e8 / 3)

    t = t_ns * 1e-9

    fig, axes = subplots(1, figsize=(12, 6))
    axes.set_xlim(0, txline.l)
    axes.set_ylim(0, 40)
    axes.set_xlabel('Distance (m)')
    axes.set_ylabel('Time (ns)')
    axes.set_title('$\Gamma_l = %.2f, \Gamma_s %.2f$' %
                   (txline.GammaVl, txline.GammaVs))

    Nbounces = int(t // txline.T)

    t0 = 0
    for bounce in range(Nbounces):
        if (bounce & 1) == 0:
            axes.plot((0, txline.l), (t0 * 1e9, (t0 + txline.T) * 1e9),
                      color='C0')
        else:
            axes.plot((txline.l, 0), (t0 * 1e9, (t0 + txline.T) * 1e9),
                      color='C1')
        t0 += txline.T

    tp = t % txline.T
    if (Nbounces & 1) == 0:
        x = tp * txline.v
        axes.plot((0, x), (t0 * 1e9, t * 1e9), color='C0')
    else:
        x = txline.l - tp * txline.v
        axes.plot((txline.l, x), (t0 * 1e9, t * 1e9), color='C1')
    axes.grid(True)
    Vp = txline.Vpulse(Vd, t)
    axes.plot(x, t * 1e9, 'o')

    if abs(Vp) < 0.1:
        Vtext = '%.2f V' % Vp
    else:
        Vtext = '%.1f V' % Vp

    axes.annotate(Vtext, (x, t * 1e9 + 2))


def txline_lattice_demo1():
    interact(txline_lattice_demo1_plot, Z0=[50, 60, 80, 100],
             Rs=[0, 10, 20, 30, 40, 50, 60, 80, 100],
             Rl=[0, 10, 20, 30, 40, 50, 60, 80, 100, 1000000],
             t_ns=(0, 40, 1),
             continuous_update=False)
