import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.style.use('seaborn-dark-palette')

font = {'family': 'normal',
        'weight': 'normal',
        'size'  : 16}
plt.tight_layout()

mpl.rc('font', **font)

sns.set_style("whitegrid")

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

pd.options.display.float_format = '{:,.3f}'.format
