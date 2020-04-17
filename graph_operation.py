import networkx as nx
import matplotlib.pyplot as plt

n = 5

#完全グラフ
Ga = nx.complete_graph(n)

#ladder graph
Gb = nx.ladder_graph(n)

plt.subplot(1, 2, 1)
plt.title("Ga:complete graph", fontweight='bold')
nx.draw(Ga, with_labels=True)
plt.subplot(1, 2, 2)
plt.title("Gb:ladder graph", fontweight='bold')
nx.draw(Gb, with_labels=True)
plt.show()

#subgraph
nbunch = [1, 2, 3, 4]
H = nx.subgraph(Ga, nbunch)
plt.subplot(1, 2, 1)
plt.title("Ga:complete graph", fontweight='bold')
nx.draw(Ga, with_labels=True)
plt.subplot(1, 2, 2)
plt.title("subgraph", fontweight='bold')
nx.draw(H, with_labels=True)
plt.show()

#union
fig = plt.figure()
H = nx.union(Ga, Gb, rename=('a-','b-'))
nx.draw(H, with_labels=True)
fig.text(0.05, 0.90, "graph union", fontweight='bold')
plt.show()

#disjoint_union
fig = plt.figure()
H = nx.disjoint_union(Ga, Gb)
nx.draw(H, with_labels=True)
fig.text(0.05, 0.90, "disjoint union", fontweight='bold')
plt.show()

#cartesian product
fig = plt.figure()
H = nx.cartesian_product(Ga, Gb)
nx.draw(H, with_labels=True)
fig.text(0.05, 0.90, "cartesian product", fontweight='bold')
plt.show()

#compose
fig = plt.figure()
H = nx.compose(Ga, Gb)
nx.draw(H, with_labels=True)
fig.text(0.05, 0.90, "compose", fontweight='bold')
plt.show()

#complement
H = nx.complement(Gb)
plt.subplot(1, 2, 1)
plt.title("Gb:ladder graph", fontweight='bold')
nx.draw(Gb, with_labels=True)
plt.subplot(1, 2, 2)
plt.title("complement", fontweight='bold')
nx.draw(H, with_labels=True)
plt.show()

#create empty copy
H = nx.create_empty_copy(Gb)
plt.subplot(1, 2, 1)
plt.title("Gb:ladder graph", fontweight='bold')
nx.draw(Gb, with_labels=True)
plt.subplot(1, 2, 2)
plt.title("create empty copy", fontweight='bold')
nx.draw(H, with_labels=True)
plt.show()

#create empty copy
H = nx.to_directed(Ga)
plt.subplot(1, 2, 1)
plt.title("Ga:undirected graph", fontweight='bold')
nx.draw(Ga, with_labels=True)
plt.subplot(1, 2, 2)
plt.title("directed graph", fontweight='bold')
nx.draw(H, with_labels=True)
plt.show()
