import networkx as nx
import matplotlib.pyplot as plt

n = 5

#完全グラフ
G = nx.complete_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "complete graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()

#balanced tree
G = nx.balanced_tree(n, 2)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "balanced tree", fontweight='bold')
fig.text(0.02, 0.90, "r-aray (r="+str(n)+")")
fig.text(0.02, 0.85, "height=2")
plt.show()

#barbell graph
G = nx.barbell_graph(n, 3)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.15, "barbell graph", fontweight='bold')
fig.text(0.02, 0.1, "two complete_graphs of "+str(n)+"(m1) nodes")
fig.text(0.02, 0.05, "3(m2) nodes between them")
plt.show()

#binomial tree
G = nx.binomial_tree(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.1, "binomial tree", fontweight='bold')
fig.text(0.02, 0.05, "n(node count) = "+str(n))
plt.show()

#complete multipartite graph
G = nx.complete_multipartite_graph(1, 2, 3)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.1, "complete multipartite graph", fontweight='bold')
fig.text(0.02, 0.05, "three subsets whose node counts are 1, 2, and 3")
plt.show()

#circular ladder graph
G = nx.circular_ladder_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "circular ladder graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()

#circulant graph
G = nx.circulant_graph(10, [1, 2])
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "circulant graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count):10 with offset:1, 2")
plt.show()

#cycle graph
G = nx.cycle_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "cycle graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()

#dorogovtsev_goltsev_mendes_graph
G = nx.dorogovtsev_goltsev_mendes_graph(3)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "dorogovtsev goltsev mendes graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = 3")
plt.show()

#full rary_tree
G = nx.full_rary_tree(3, 7)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "full rary tree", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n)+", with 3-ary")
plt.show()

#ladder graph
G = nx.ladder_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "ladder graph", fontweight='bold')
fig.text(0.02, 0.90, "n(ladder count) = "+str(n))
plt.show()

#lollipop graph
G = nx.lollipop_graph(n, 3)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "lollipop graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node cout) = "+str(n))
plt.show()

#path graph
G = nx.path_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "path graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()

#star graph
G = nx.star_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "star graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()

#turan graph
G = nx.turan_graph(n, 2)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "turan graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
fig.text(0.02, 0.85, "with 2 disjoint subset")
plt.show()

#wheel graph
G = nx.wheel_graph(n)
fig = plt.figure()
nx.draw(G, with_labels=True)
fig.text(0.02, 0.95, "wheel graph", fontweight='bold')
fig.text(0.02, 0.90, "n(node count) = "+str(n))
plt.show()
