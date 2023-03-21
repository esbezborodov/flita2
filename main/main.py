import pandas as pd
from numpy import genfromtxt
import matplotlib.pyplot as plt
import networkx as nx


mydata = genfromtxt('file.txt', delimiter=' ')
G = nx.DiGraph(mydata)
print(G)
nx.draw(G, with_labels=True)
plt.show()
