# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_loading_demo_plot(model=models[0], RL=100, VL=0):

    Vdd = 3.3
    case = 'typ'

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    fig, ax = subplots(1)
    model_case.output_IV_curves_plot(ax)
    model_case.output_IV_load_plot(ax, Rload=RL, Vload=VL)
    ax.set_title(model_case.title)


def IV_loading_demo():
    interact(IV_loading_demo_plot, model=models, case=['typ', 'min', 'max'],
             RL=(10, 200, 10), VL=(0, 3.5, 0.5),
             continuous_update=False)
