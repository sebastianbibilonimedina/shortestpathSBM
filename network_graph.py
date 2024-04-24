import networkx as nx

CITIES = ["WA", "CA1", "CA2", "UT", "CO", "TX", "NE", "IL", "PA",
          "GA", "MI", "NY", "NJ", "DC"]
EDGES = [
    ("WA", "CA1", 1050),
    ("CA1", "CA2", 600),
    ("WA", "CA2", 1500),
    ("CA1", "UT", 750),
    ("WA", "IL", 2400),
    ("UT", "MI", 1950),
    ("UT", "CO", 600),
    ("CA2", "TX", 1800),
    ("CO", "NE", 600),
    ("CO", "TX", 1200),
    ("NE", "IL", 750),
    ("NE", "GA", 1350),
    ("TX", "DC", 1800),
    ("TX", "GA", 1050),
    ("IL", "PA", 750),
    ("PA", "NJ", 300),
    ("PA", "NY", 300),
    ("MI", "NY", 600),
    ("MI", "NJ", 750),
    ("NY", "DC", 300),
    ("NJ", "DC", 150),
    ("PA", "GA", 750)
]


def add_nodes_to_graph(network_graph, nodes):
    network_graph.add_nodes_from(nodes)


def add_edges_to_graph(network_graph, edges):
    network_graph.add_weighted_edges_from(edges)


def create_network_graph():
    # Create an empty graph object
    network_graph = nx.Graph()

    # Add nodes to the graph
    add_nodes_to_graph(network_graph, CITIES)

    # Add edges with distances between cities
    add_edges_to_graph(network_graph, EDGES)

    return network_graph


network_graph = create_network_graph()