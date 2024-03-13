import networkx as nx
import matplotlib.pyplot as plt

def create_knight_graph():
    """
    Create a graph representing the movements of a knight on a chessboard.

    Returns:
        networkx.Graph: The knight graph.
    """
    knight_graph = nx.Graph()
    knight_graph.add_nodes_from([k for k in range(1, 65)])

    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
             (1, -2), (2, -1), (2, 1), (1, 2)]

    for i in range(8):
        for j in range(8):
            current_node = i*8 + j + 1

            for move in moves:
                new_i, new_j = i + move[0], j + move[1]

                if 0 <= new_i < 8 and 0 <= new_j < 8:
                    neighbor_node = new_i*8 + new_j + 1
                    knight_graph.add_edge(current_node, neighbor_node)

    return knight_graph

def draw_graph(G, file_name):
    """
    Draw the graph and save it as an image file.

    Parameters:
        G (networkx.Graph): The input graph.
        file_name (str): Name of the output image file.
    """
    pos = {}

    for i in range(8):
        for j in range(8):
            pos[i * 8 + j + 1] = (j, -i)

    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', edge_color='black', font_size=12,
                     font_weight='bold', node_size=500, alpha=0.7)

    plt.savefig(file_name)
