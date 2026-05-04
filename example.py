from bnbvisual import *

# Define nodes
raw_nodes = {
    0:     ("Node 0", -28, (0.67, 0, 1, 1), {0: "root"}),
    1:     ("Node 1", -27.6, (0, 0.8, 1, 1), {1: "fractional"}),
    2:     ("Node 2", -14.67, (1, 0, 0.5, 1), {1: "fractional"}),
    1_1:   ("Node 1-1", -18, (0, 0, 1, 1), {2: "incumbent", 5: "pruned"}),
    1_2:   ("Node 1-2", -27.5, (0, 1, 0.75, 1), {2: "fractional"}),
    2_1:   ("Node 2-1", -27.8, (1, 0.4, 0, 1), {3: "fractional"}),
    2_2:   ("Node 2-2", -27.6, (1, 0, 1, 0.33), {3: "fractional"}),
    1_2_1: ("Node 1-2-1", -20, (0, 1, 0, 1), {4: "incumbent", 6: "pruned"}),
    1_2_2: ("Node 1-2-2", -27.33, (0, 1, 1, 0.67), {4: "fractional"}),
    2_1_1: ("Node 2-1-1", -23, (1, 0, 0, 1), {6: "incumbent", 7: "pruned"}),
    2_1_2: ("Node 2-1-2", -27, (1, 1, 0, 0), {7: "incumbent"}),
    2_2_1: ("Node 2-2-1", -27.4, (1, 0.2, 1, 0), {8: "fractional"}),
    2_2_2: ("Node 2-2-2", "N/A", None, {8: "infeasible"}),
    1_2_2_1: ("Node 1-2-2-1", -22, (0, 1, 1, 0), {9: "pruned"}),
    1_2_2_2: ("Node 1-2-2-2", "N/A", None, {9: "infeasible"}),
    2_2_1_1: ("Node 2-2-1-1", "N/A", None, {9: "infeasible"}),
    2_2_1_2: ("Node 2-2-1-2", "N/A", None, {9: "infeasible"})
}

# Define edges
edges = [
    (0, 1, r"$x_{1} = 0$"), (0, 2, r"$x_{1} = 1$"),
    (1, 1_1, r"$x_{2} = 0$"),     (1, 1_2, r"$x_{2} = 1$"),
    (2, 2_1, r"$x_{3} = 0$"),     (2, 2_2, r"$x_{3} = 1$"),
    (1_2, 1_2_1, r"$x_{3} = 0$"), (1_2, 1_2_2, r"$x_{3} = 1$"),
    (2_1, 2_1_1, r"$x_{2} = 0$"), (2_1, 2_1_2, r"$x_{2} = 1$"),
    (2_2, 2_2_1, r"$x_{4} = 0$"), (2_2, 2_2_2, r"$x_{4} = 1$"),
    (1_2_2, 1_2_2_1, r"$x_{4} = 0$"), (1_2_2, 1_2_2_2, r"$x_{4} = 1$"),
    (2_2_1, 2_2_1_1, r"$x_{2} = 0$"), (2_2_1, 2_2_1_2, r"$x_{2} = 1$")
]

# Generate layout from nodes and edges
nodes, tree_width = generate_tree_layout(raw_nodes, edges)
canvas_width = max(10, tree_width * 1.05) 

# Define the node revealing sequence
reveal_sequence = [
    [0],  
    [1, 2], 
    [1_1, 1_2],
    [2_1, 2_2],
    [1_2_1, 1_2_2],
    [],
    [2_1_1],
    [2_1_2],
    [2_2_1, 2_2_2],
    [1_2_2_1, 1_2_2_2],
    [2_2_1_1, 2_2_1_2]
]

# Draw the tree incrementally
draw_bnb_incremental(
    all_nodes=nodes, 
    all_edges=edges, 
    reveal_order=reveal_sequence, 
    filename="bnb_ex4",
    figsize=(canvas_width, 8)
)
