import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

white = '#ffffff'
mpl.rc('axes', facecolor=white)

y = [0.85, 0.92, 0.95, 0.977]
x = np.arange(4)
labels = ['Baseline', 'Iteration 1', 'Iteration 2', 'Iteration 3']
width = 0.5
color = '#000067'
ylabel = 'AUC'

plt.bar(x, y, width, color=color)
plt.xticks(x)
plt.gca().set_xticklabels(labels)
plt.ylabel(ylabel)

plt.ylim([0.5, 1.0])

plt.show()

