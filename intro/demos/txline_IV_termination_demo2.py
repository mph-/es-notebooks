# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import inf, linspace, zeros

filenames = {'sam4s': 'data/sam4s16.ibs'}


def txline_IV_termination_demo2_plot(Z0=60, R1=120):

    Vdd = 3.3
    case = 'typ'
    model = 'sam4s pa0'

    if R1 < Z0:
        print('Invalid resistor value')

    if R1 == Z0:
        R2 = inf
        Vt = Vdd
    else:
        R2 = (R1 * Z0) / (R1 - Z0)
        Vt = R2 * Vdd / (R1 + R2)

        print('R2 = %s ohms, Vt = %s V' % (round(R2, 2), Vt))

    if R2 is inf:
        R2 = 1e8

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    fig, axes = subplots(1, 2, figsize=(12, 5))
    model_case.output_IV_curves_plot(axes[0])
    model_case.output_IV_load_plot(axes[0], Rload=Z0, Vload=Vt)
    axes[0].set_title(model_case.title)

    tx = linspace(0, 10e-9, 301)
    Vo = zeros(len(tx))
    Io = zeros(len(tx))
    Vl = zeros(len(tx))

    mr = tx < 5e-9
    Vo[mr], Io[mr], Vl[mr] = model_case.step_rise(tx[mr], Cload=5e-12, Rs=0,
                                                  Rt=Z0, Vt=Vt)
    mf = tx >= 5e-9
    Vo[mf], Io[mf], Vl[mf] = model_case.step_fall(tx[mf], Cload=5e-12, Rs=0,
                                                  Rt=Z0, Vt=Vt)

    axes[1].plot(tx * 1e9, Vl)
    axes[1].set_xlabel('Time (ns)')
    axes[1].set_ylabel('Voltage (V)')
    axes[1].grid(True)
    axes[1].set_ylim(0, 3.5)


def txline_IV_termination_demo2():
    interact(txline_IV_termination_demo2_plot,
             Z0=[60, 80, 100],
             R1=[60, 80, 100, 120, 160, 200, 240, 1000000],
             continuous_update=False)
