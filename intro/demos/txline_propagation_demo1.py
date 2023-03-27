# M. P. Hayes UCECE
from ipywidgets import interact
from IPython.display import Image, display


def txline_propagation_demo1_plot(timestep=0):

    filenames = {0: 'figs/lossless_txline_unbalanced3a.png',
                 1: 'figs/lossless_txline_unbalanced3b.png',
                 2: 'figs/lossless_txline_unbalanced3c.png',
                 3: 'figs/lossless_txline_unbalanced3d.png',
                 4: 'figs/lossless_txline_unbalanced3e.png',
                 5: 'figs/lossless_txline_unbalanced3f.png',
                 6: 'figs/lossless_txline_unbalanced3g.png',
                 7: 'figs/lossless_txline_unbalanced3h.png',
                 8: 'figs/lossless_txline_unbalanced3i.png',
                 9: 'figs/lossless_txline_unbalanced3j.png',
                 10: 'figs/lossless_txline_unbalanced3k.png',
                 11: 'figs/lossless_txline_unbalanced3l.png',
                 12: 'figs/lossless_txline_unbalanced3m.png',
                 13: 'figs/lossless_txline_unbalanced3n.png',
                 14: 'figs/lossless_txline_unbalanced3o.png',
                 15: 'figs/lossless_txline_unbalanced3p.png'}

    filename = filenames[timestep]
    image = Image(filename=filename)
    display(image)


def txline_propagation_demo1():
    interact(txline_propagation_demo1_plot, timestep=(0, 15, 1),
             continuous_update=False)
