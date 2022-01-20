# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_resistance_demo_plot(model=models[0]):

    Vdd = 3.3
    case = 'typ'

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    fig, ax = subplots(1)
    model_case.output_resistance_plot(ax)
    ax.set_title(model_case.title)
    ax.set_ylim(0, 200)


def IV_resistance_demo():
    interact(IV_resistance_demo_plot, model=models, continuous_update=False)
