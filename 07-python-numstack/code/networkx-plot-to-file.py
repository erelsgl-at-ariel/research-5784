import networkx as nx
import matplotlib.pyplot as plt
mygraph = nx.complete_graph(6)   

nx.draw(mygraph)
plt.savefig("mygraph.png")
