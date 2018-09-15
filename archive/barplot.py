import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('ggplot')

gray = '#f7f8f9'
mpl.rc('axes', facecolor=gray)

y = [0.85, 0.92, 0.95, 0.977]
x = np.arange(4)
labels = ['Benchmark', 'Diluted CNN', 'LSTM encoder', 'LSTM with embeddings']
width = 0.5
color = '#000067'
ylabel = 'AUC'

plt.bar(x, y, width, color=color)
plt.xticks(x)
plt.gca().set_xticklabels(labels)
plt.ylabel(ylabel)

plt.show()
