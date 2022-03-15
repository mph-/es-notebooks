# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import linspace

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s': 'data/sam4s16.ibs'}


def risetime_demo4_plot(model=models[0], C_comp_pF=2, L_pkg_nH=1,
                        R_pkg=0.1, C_pkg_pF=0.5, Cl_pF=5, Rs=5,
                        t_ns=1e-9):

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
    Vo, Io, Vl = model_case.step_response_with_parasitics(
        'rise', tx,
        Cload=Cl_pF * 1e-12,
        Rs=Rs,
        Ccomp=C_comp_pF * 1e-12,
        Lpkg=L_pkg_nH * 1e-9,
        Cpkg=C_pkg_pF * 1e-12,
        Rpkg=R_pkg)

    axes[1].plot(tx * 1e9, Vl, label='Vl')
    axes[1].plot(tx * 1e9, Vo, '--', label='Vo')
    axes[1].set_xlabel('Time (ns)')
    axes[1].set_ylabel('Voltage (V)')
    axes[1].grid(True)
    axes[1].set_ylim(0, 3.5)
    axes[1].legend()

    Io = model_case.Ioutput_high(Vo[m])

    axes[0].plot(Vo[m], Io * 1e3, 'ko')
    axes[1].plot(t * 1e9, Vo[m], 'ko')

    axes[0].set_title(model_case.title)
    fig.tight_layout()


def risetime_demo4():
    interact(risetime_demo4_plot, model=models,
             Cl_pF=[5, 50, 5],
             C_comp_pF=[1, 2, 3, 4, 5],
             L_pkg_nH=[0.5, 1, 2, 4],
             R_pkg=[0.05, 0.1, 0.2],
             C_pkg_pF=[0.5, 1, 2],
             Rs=[0, 1, 5, 10, 50, 100, 500, 1000],
             t_ns=(0, 2, 0.2),
             continuous_update=False)
