import matplotlib.pyplot as plt
import networkx as nx

n = 7
G = nx.wheel_graph(n)

##### add color to nodes
G.nodes[0]['color'] = 'r'
G.nodes[1]['color'] = 'b'
G.nodes[2]['color'] = 'g'
G.nodes[3]['color'] = 'b'
G.nodes[4]['color'] = 'g'
G.nodes[5]['color'] = 'b'
G.nodes[6]['color'] = 'g'

##### add weight to edges
G.add_weighted_edges_from([(0, 1, 0.1), (0, 2, 0.1), (0, 3, 0.1), (0, 4, 0.1), (0, 5, 0.1), (0, 6, 0.1)])
G.add_weighted_edges_from([(1, 2, 0.8), (2, 3, 0.8), (3, 4, 0.8), (4, 5, 0.8), (5, 6, 0.8), (6, 1, 0.8)])

#### draw nodes
#extract node color list
node_color_list = [v['color'] for (u, v) in G.nodes(data=True)]

# positions for all nodes
pos = nx.spring_layout(G)  # positions for all nodes

# draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_color_list)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

#### draw edges
#divide edges into two types
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

# draw edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, stype='dashed')
nx.draw_networkx_edges(G, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b')

edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
