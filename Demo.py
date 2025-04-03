import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes (representing function calls in the recursion tree)
nodes = {
    "pzz(2)": (0, 3),
    "pzz(1)_L": (-2, 2),
    "pzz(1)_R": (2, 2),
    "pzz(0)_LL": (-3, 1),
    "pzz(0)_LR": (-1, 1),
    "pzz(0)_RL": (1, 1),
    "pzz(0)_RR": (3, 1),
}

# Define edges (representing function calls and returns)
edges = [
    ("pzz(2)", "pzz(1)_L"),
    ("pzz(2)", "pzz(1)_R"),
    ("pzz(1)_L", "pzz(0)_LL"),
    ("pzz(1)_L", "pzz(0)_LR"),
    ("pzz(1)_R", "pzz(0)_RL"),
    ("pzz(1)_R", "pzz(0)_RR"),
]

# Add nodes to the graph
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(6, 6))
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=8, font_weight="bold")

# Show plot
plt.title("Recursion Tree for pzz(2)")
plt.show()
