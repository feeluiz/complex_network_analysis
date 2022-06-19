import networkx as nx

def get_graph_by_file(filename):
    """Load the data set file in to a NetworkX Graph.

    @param: filename: place the dataset .net file
    Returns
    -------
    G : NetworkX MultiGraph or MultiDiGraph.
    """
    return nx.read_pajek(filename)

def get_graph_geometries(G):
    """Generate Graph Geometry.

    @param: G: NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    Returns
    -------
    positions : dict
        A dictionary of positions keyed by node
    """
    return nx.spring_layout(G)

