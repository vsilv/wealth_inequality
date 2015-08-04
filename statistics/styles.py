import matplotlib.pyplot as plt
%matplotlib inline
%load_ext autoreload
%autoreload 2
from matplotlib.colors import colorConverter
import prettyplotlib as ppl
from matplotlib import rcParams
import seaborn as sns

sns.set(style='ticks', palette='Set2') 
sns.despine()
import itertools
# These are the colors. Notice how this is programmed:
# You initialize your colors by 
# colorset = palette()
# then you can cycle through the colors:
# color = next(colorset)
# if you want your set to be reset, just create
# a new palette() instance! This way the colors do not interfere.

color_names = ['windows blue', "pale red", "faded green", "amber", 
          'dark green', 'dark fuchsia', 'browny orange', 
          'puke green', 'dark royal blue', 'dusty purple', 
               'red orange','dark grey','blue grey', 'bright purple', 'chocolate brown',
              'shit', 'pistachio','stone','asparagus','butter']

colors = sns.xkcd_palette(color_names)
palette = lambda: itertools.cycle(sns.xkcd_palette(color_names) )

fontsize_labels = 26    # size used in latex document
rcParams['text.latex.preamble'] = [r'\usepackage[cmbright]{sfmath}']
rcParams['font.family']= 'sans-serif'
rcParams['font.sans-serif']= 'cmbright'
rcParams['font.weight'] = "light"

rcParams['text.usetex'] = True

rcParams['figure.autolayout'] = True
rcParams['font.size'] = fontsize_labels
rcParams['axes.labelsize'] = fontsize_labels
rcParams['xtick.labelsize'] = fontsize_labels
rcParams['ytick.labelsize'] = fontsize_labels
rcParams['legend.fontsize'] = fontsize_labels
rcParams['legend.markerscale'] = 4
rcParams['axes.titlesize'] = fontsize_labels
rcParams['text.color'] = "0.3"
rcParams['xtick.color'] = "0.3"
rcParams['ytick.color'] = "0.3"
rcParams['axes.labelcolor'] = "0.3"
rcParams['axes.edgecolor'] = "0.8"
rcParams['axes.formatter.limits'] = (-2,3)

xfactor = 2
rcParams['figure.figsize'] = (xfactor*6.2, xfactor*3.83)  

fig_dir = "../report/figures/analysis/"  # directory of figures
save_fig = True

def savefig(filename):
    if save_fig == True:
        plt.savefig(fig_dir+filename+".pdf")


def fixticks(ax):    
    for t in ax.xaxis.get_ticklines(): t.set_color('0.8')
    for t in ax.yaxis.get_ticklines(): t.set_color('0.8')
