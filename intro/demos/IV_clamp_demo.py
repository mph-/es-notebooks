# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import linspace

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_clamp_demo_plot(model=models[0]):

    Vdd = 3.3
    case = 'typ'

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    V = linspace(0 - 1.5, Vdd + 1.5, 200)

    fig, ax = subplots(1)
    model_case.output_IV_curves_plot(ax, V=V)
    ax.set_title(model_case.title)


def IV_clamp_demo():
    interact(IV_clamp_demo_plot, model=models, continuous_update=False)
