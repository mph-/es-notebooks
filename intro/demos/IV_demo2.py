# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_demo2_plot(model=models[0], typ=True, min=False, max=False,
                  Rload=100, Vload=0):

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

    model_case.output_IV_load_plot(ax, Rload=Rload, Vload=Vload)
    ax.set_title(model_case.title)


def IV_demo2():
    interact(IV_demo2_plot, model=models,
             Rload=(10, 200, 10), Vload=(0, 3.5, 0.5),
             continuous_update=False)
