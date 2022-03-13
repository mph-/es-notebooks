# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import linspace

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s': 'data/sam4s16.ibs'}


def risetime_demo1_plot(model=models[0], CL_pF=5, t_ns=1e-9):

    Vdd = 3.3
    case = 'typ'

    t = t_ns * 1e-9
    tx = linspace(0, 10e-9, 301)
    dt = tx[1] - tx[0]
    m = int(t / dt + 0.5)

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    fig, axes = subplots(1, 2, figsize=(12, 5))
    model_case.output_IV_curves_plot(axes[0], high=True)
    Vo, Io, Vl = model_case.step_rise(tx, Cload=CL_pF * 1e-12)

    axes[1].plot(tx * 1e9, Vo)
    axes[1].set_xlabel('Time (ns)')
    axes[1].set_ylabel('Voltage (V)')
    axes[1].grid(True)
    axes[1].set_ylim(0, 3.5)

    Io = model_case.Ioutput_high(Vo[m])

    axes[0].plot(Vo[m], Io * 1e3, 'ko')
    axes[1].plot(t * 1e9, Vo[m], 'ko')

    axes[0].set_title(model_case.title)
    fig.tight_layout()


def risetime_demo1():
    interact(risetime_demo1_plot, model=models, CL_pF=(5, 50, 5),
             t_ns=(0, 2, 0.2), continuous_update=False)
