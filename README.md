# Minimum paths for a knight on a chessboard

## Goal

Given two squares $s_1$ and $s_2$ of an $8\times 8$ chessboard, find all the simple paths (i.e., with no repeating squares) connecting $s_1$ and $s_2$ via legal knight moves.

## Overview of the solution

The challenge can be mapped into a simple combinatorial problem by considering the graph where each node corresponds to a square in the chessboard and two nodes are adjacent if and only if there is a legal knight move connecting them. Once such a graph has been constructed, the minimum paths connecting the input squares can then be obtained by means of the standard Dijkstra's algorithm.

## Requirements

The code relies on the Python libraries `numpy`, `networkx` and `matplotlib`. The package graphviz is also necessary to convert the output .dot file into an .ps image of the requested graph.

## Implementation details

Four scripts are included in the project:

- `graph_setup.py`, with the functions necessary to build the graph and draw it;
- `pathfinding.py`, implementing the main algorithm;
- `visualization.py`, containing all the functions necessary to create the output images;
- `main.py` to build the output files.

The chessboard is indexed with numbers $1, 2, ..., 64$ corresponding to the squares $\mathrm a1, \mathrm a2, ..., \mathrm h8$ according to the following table:

$$\begin{bmatrix}
8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 \\
7 & 15 & 23 & 31 & 39 & 47 & 55 & 63 \\
6 & 14 & 22 & 30 & 38 & 46 & 54 & 62 \\
5 & 13 & 21 & 29 & 37 & 45 & 53 & 61 \\
4 & 12 & 20 & 28 & 36 & 44 & 52 & 60 \\
3 & 11 & 19 & 27 & 35 & 43 & 51 & 59 \\
2 & 10 & 18 & 26 & 34 & 42 & 50 & 58 \\
1 & 9 & 17 & 25 & 33 & 41 & 49 & 57 \\
\end{bmatrix}
\quad \Leftrightarrow \quad 
\begin{bmatrix}
\mathrm{a}8 & \mathrm{b}8 & \mathrm{c}8 & \mathrm{d}8 & \mathrm{e}8 & \mathrm{f}8 & \mathrm{g}8 & \mathrm{h}8 \\
\mathrm{a}7 & \mathrm{b}7 & \mathrm{c}7 & \mathrm{d}7 & \mathrm{e}7 & \mathrm{f}7 & \mathrm{g}7 & \mathrm{h}7 \\
\mathrm{a}6 & \mathrm{b}6 & \mathrm{c}6 & \mathrm{d}6 & \mathrm{e}6 & \mathrm{f}6 & \mathrm{g}6 & \mathrm{h}6 \\
\mathrm{a}5 & \mathrm{b}5 & \mathrm{c}5 & \mathrm{d}5 & \mathrm{e}5 & \mathrm{f}5 & \mathrm{g}5 & \mathrm{h}5 \\
\mathrm{a}4 & \mathrm{b}4 & \mathrm{c}4 & \mathrm{d}4 & \mathrm{e}4 & \mathrm{f}4 & \mathrm{g}4 & \mathrm{h}4 \\
\mathrm{a}3 & \mathrm{b}3 & \mathrm{c}3 & \mathrm{d}3 & \mathrm{e}3 & \mathrm{f}3 & \mathrm{g}3 & \mathrm{h}3 \\
\mathrm{a}2 & \mathrm{b}2 & \mathrm{c}2 & \mathrm{d}2 & \mathrm{e}2 & \mathrm{f}2 & \mathrm{g}2 & \mathrm{h}2 \\
\mathrm{a}1 & \mathrm{b}1 & \mathrm{c}1 & \mathrm{d}1 & \mathrm{e}1 & \mathrm{f}1 & \mathrm{g}1 & \mathrm{h}1 \\
\end{bmatrix}. $$

The program will accept inputs *both* in algebraic notation (e.g. $\mathrm a1$, $\mathrm B7$ or $\mathrm H3$ with or without capitalization) and in integer form, and will output the following files in the working directory:

- `shortest_paths.dot` and the corresponding `shortest_path.ps` containing the directed graph representing the minimum paths (you can choose to allow or disallow multiple arrows between the same nodes at runtime);
- `knight_graph.png`, an image of the graph underlying the program;
- `shortest_paths_chessboard.png`, an image of the directed paths over an annotated chessboard, together with information about the number of paths and their length (including the starting and ending squares).

You will find the output corresponding to the case $\mathrm a1\to \mathrm h8$ already uploaded as a reference.

## Usage 

Simply run the main file in order to generate the aforementioned output images. For Docker users, a Dockerfile is included in the project. The following steps are required in order to build and run a docker container:

- Make sure Docker is installed and active on your machine (run `sudo docker run hello-world` to check everything is working as expected).
- In the project folder, run the command `sudo docker build -t my_project_image` to build the container. The -t option tags the container with the specified string `my_project_image`.
- Run `sudo docker run -it my_project_image .` to launch the program. You will be prompted to enter the squares (as mentioned, both algebraic and numerical notations are fine): note that the -it flag is essential to interact with the program.
- Run `sudo docker ps -a` to see the ID corresponding to the generated container.
- Finally, copy the contents in the desired location with the syntax: `sudo docker cp container_id:/container/path /host/path`. Example: if the container ID is 028a78bc0f1a, the output .ps file can be copied locally with
`sudo docker cp 028a78bc0f1a:/app/shortest_paths.ps /host/path`.





