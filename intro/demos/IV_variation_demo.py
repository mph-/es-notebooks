# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_variation_demo_plot(model=models[0], typ=True, min=False, max=False):

    Vdd = 3.3

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)

    fig, ax = subplots(1)
    if min:
        model_case = model.case(case='min')
        model_case.output_IV_curves_plot(ax, linestyle='--', label='min')

    if typ:
        model_case = model.case(case='typ')
        model_case.output_IV_curves_plot(ax, label='typ')

    if max:
        model_case = model.case(case='max')
        model_case.output_IV_curves_plot(ax, linestyle='-.', label='max')
    ax.legend()

    ax.set_title(model_case.title)


def IV_variation_demo():
    interact(IV_variation_demo_plot, model=models,
             continuous_update=False)
