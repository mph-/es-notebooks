# M. P. Hayes UCECE
from ipywidgets import interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import inf

filenames = {'sam4s': 'data/sam4s16.ibs'}


def txline_IV_termination_demo1_plot(R1=120):

    Z0 = 60
    Vdd = 3.3
    case = 'typ'
    model = 'sam4s pa0'

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

    fig, ax = subplots(1)
    model_case.output_IV_curves_plot(ax)
    model_case.output_IV_load_plot(ax, Rload=Z0, Vload=Vt)
    ax.set_title(model_case.title)


def txline_IV_termination_demo1():
    interact(txline_IV_termination_demo1_plot,
             R1=[60, 80, 100, 120, 240, 1000000],
             continuous_update=False)
