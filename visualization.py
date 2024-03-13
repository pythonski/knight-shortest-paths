import numpy as np
import matplotlib.pyplot as plt

def generate_dot_file(paths, file_name, multiple_arrows=False):
    """
    Generate a .dot file representing the paths in a graph.

    Parameters:
        paths (list of lists): List of paths, where each path is represented as a list of node indices.
        file_name (str): Name of the output .dot file.
        multiple_arrows (bool, optional): If True, allows multiple arrows between the same nodes. Defaults to False.
    """
    dot_content = "digraph shortest_paths {\n"
    added_edges = set()

    for path in paths:
        for i in range(len(path) - 1):
            start_node = path[i]
            end_node = path[i + 1]
            edge = (start_node, end_node)

            if multiple_arrows or edge not in added_edges:
                dot_content += f"\t{integer_to_chess_notation(start_node)} -> {integer_to_chess_notation(end_node)};\n"

                if not multiple_arrows:
                    added_edges.add(edge)

    dot_content += "}\n"

    with open(file_name, "w") as file:
        file.write(dot_content)

def draw_arrow(ax, start, end, color='red'):
    """
    Draw an arrow between two points on a plot.

    Parameters:
        ax (matplotlib.axes.Axes): The Axes object to draw on.
        start (tuple): Coordinates of the starting point (x, y).
        end (tuple): Coordinates of the ending point (x, y).
        color (str, optional): Color of the arrow. Defaults to 'red'.
    """
    ax.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1], head_width=0.1, head_length=0.1, fc=color, ec=color)

def draw_circle(ax, center, color='red'):
    """
    Draw a circle on a plot.

    Parameters:
        ax (matplotlib.axes.Axes): The Axes object to draw on.
        center (tuple): Coordinates of the center of the circle (x, y).
        color (str, optional): Color of the circle. Defaults to 'red'.
    """
    ax.add_patch(plt.Circle(center, 0.2, color=color, fill=False))

def visualize_paths(paths, file_name):
    """
    Visualize paths on a chessboard-like grid and save the plot to a file.

    Parameters:
        paths (list of lists): List of paths, where each path is represented as a list of node indices.
        file_name (str): Name of the output image file.
    """
    grid = np.zeros((8, 8))

    # Filling in the black squares
    grid[1::2, ::2] = 1
    grid[::2, 1::2] = 1

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(grid, cmap='binary', origin='lower')

    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    ax.set_yticklabels(['1', '2', '3', '4', '5', '6', '7', '8'])

    for path in paths:
        for i in range(len(path) - 1):
            start_square = (path[i] - 1) // 8, (path[i] - 1) % 8
            end_square = (path[i+1] - 1) // 8, (path[i+1] - 1) % 8
            draw_arrow(ax, start_square, end_square)

        start_point = (path[0] - 1) // 8, (path[0] - 1) % 8
        end_point = (path[-1] - 1) // 8, (path[-1] - 1) % 8
        draw_circle(ax, start_point)
        draw_circle(ax, end_point)

    # Useful quantities
    path_length = len(paths[0])
    number_paths = len(paths)
    starting_square = paths[0][0]
    ending_square = paths[0][-1]

    plt.text(8, 6.5, f"Starting at: {integer_to_chess_notation(starting_square)}", fontsize=12)
    plt.text(8, 6, f"Ending at: {integer_to_chess_notation(ending_square)}", fontsize=12)
    plt.text(8, 5, f"Path length: {path_length}", fontsize=12)
    plt.text(8, 5.5, f"Number of paths: {number_paths}", fontsize=12)

    plt.savefig(file_name)

def integer_to_chess_notation(integer):
    """
    Convert an integer index to chess notation.

    Parameters:
        integer (int): Integer index representing a square on a chessboard.

    Returns:
        str: Chess notation representation of the square.
    """
    row = (integer - 1) % 8 + 1
    column = (integer - 1) // 8
    column_letter = chr(ord("a") + column)
    return f"{column_letter}{row}"

def chess_notation_to_integer(chess_notation):
    """
    Convert chess notation to an integer index.

    Parameters:
        chess_notation (str): Chess notation representing a square on a chessboard.

    Returns:
        int: Integer index representing the square.
    """
    column = ord(chess_notation[0]) - ord("a") + 1
    row = int(chess_notation[1])
    integer_representation = (column - 1) * 8 + row
    return integer_representation
