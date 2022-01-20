# M. P. Hayes UCECE
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import subplots
from mibis import IBISFile
from numpy import linspace

models = ['sam4s pa0', 'sam4s pa12', 'sam4s ddp']
filenames = {'sam4s':'data/sam4s16.ibs'}

def IV_resistance_demo2_plot(model=models[0], V=1.5):

    Vdd = 3.3
    case = 'typ'

    parts = model.split(' ')
    ibisfilename = filenames[parts[0]]
    modelname = parts[1]

    ibisfile = IBISFile(ibisfilename)
    model = ibisfile.model(modelname, Vdd)
    model_case = model.case(case=case)

    fig, axes = subplots(2)
    model_case.output_IV_curves_plot(axes[0])
    Ioh = model_case.Ioutput_high(V)
    axes[0].plot(V, Ioh * 1e3, 'ro')
    Iol = model_case.Ioutput_low(V)
    axes[0].plot(V, Iol * 1e3, 'bo')

    model_case.output_resistance_plot(axes[1])
    Roh = model_case.Routput_high(V)
    axes[1].plot(V, Roh, 'ro')
    Rol = model_case.Routput_low(V)
    axes[1].plot(V, Rol, 'bo')
    axes[1].set_ylim(0, 200)

    # Plot tangents
    V1 = linspace(V - 1, V + 1, 30)
    I1l = (V - V1) / Rol + Iol
    I1h = (V - V1) / Roh + Ioh
    axes[0].plot(V1, I1h * 1e3, 'k--')
    axes[0].plot(V1, I1l * 1e3, 'k--')
    axes[0].set_xlim(0, Vdd)

def IV_resistance_demo2():
    interact(IV_resistance_demo2_plot, model=models,
             V=(0, 3.5, 0.5), continuous_update=False)
