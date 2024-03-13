import networkx as nx

def find_shortest_paths(graph, source, target):
    """
    Find all shortest paths between a source and a target node in a graph.

    Parameters:
        graph (networkx.Graph): The input graph.
        source: The starting node for the paths.
        target: The target node for the paths.

    Returns:
        list of lists: List of paths, where each path is represented as a list of nodes.
    """
    return [p for p in nx.all_shortest_paths(graph, source, target)]

