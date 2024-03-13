import graph_setup
import pathfinding
import visualization

def main():

    # Creating the graph
    knight_graph = graph_setup.create_knight_graph()

    # Optionally: visualize the graph
    graph_setup.draw_graph(knight_graph, "knight_graph.png")

    # Handling user input
    allowed_numbers = list(range(1, 65))
    allowed_squares = [f"{chr(letter)}{number}" for letter in range(ord("a"), ord("h") + 1) for number in range(1, 9)]

    source = None
    target = None

    while source not in allowed_numbers + allowed_squares:
        source = input("Enter the first square (e.g., a1 or 1, b1 or 9, up to h8 or 64): ").lower()

        # Convert string to integer if the input is a digit
        if source.isdigit():
            source = int(source)

        if source not in allowed_numbers + allowed_squares:
            print("Invalid input. Please try again.\n")

    while target not in allowed_numbers + allowed_squares:
        target = input("Enter the second square (e.g., a1 or 1, b1 or 9, up to h8 or 64): ").lower()

        if target.isdigit():
            target = int(target)

        if target not in allowed_numbers + allowed_squares:
            print("Invalid input. Please try again.\n")

    # Convert algebraic notation into numerical notation for consistency
    if source in allowed_squares:
        source = visualization.chess_notation_to_integer(source)

    if target in allowed_squares:
        target = visualization.chess_notation_to_integer(target)

    # Choose between types of graph
    allowed_answers = ["y", "n"]
    answer = None

    while answer not in allowed_answers:
        answer = input("Allow multiple arrows between same nodes (y/n)? ").lower()

        if answer not in allowed_answers:
            print("Invalid input. Please try again.\n")

    if answer == "y":
        multiple_arrows = True

    else:
        multiple_arrows = False

    # Generating list of all minimum paths
    paths = pathfinding.find_shortest_paths(knight_graph, source, target)

    # Visualizations
    visualization.generate_dot_file(paths, "shortest_paths.dot", multiple_arrows)
    visualization.visualize_paths(paths, "shortest_paths_chessboard.png")

    print(f"Found {len(paths)} minimum paths of length {len(paths[0])}.")

if __name__ == "__main__":
    main()
