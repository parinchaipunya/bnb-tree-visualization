---
# Dynamic Branch and Bound Tree Visualizer

A Python utility for generating incremental, publication-quality visualizations of **Branch and Bound** search trees. This tool calculates optimal tree layouts and generates step-by-step frames showing the evolution of the optimization process, including node status changes (e.g., fractional, pruned, incumbent).

### ✨ Features
*   **Auto-Layout Engine:** Automatically calculates horizontal and vertical spacing based on text length to prevent overlapping nodes.
*   **Incremental Reveal:** Generates a sequence of images representing the "steps" of the algorithm.
*   **Status Tracking:** Nodes change colors based on their state (Root, Fractional, Incumbent, Pruned, Infeasible) at each specific step.
*   **Symmetrical Framing:** Maintains a consistent viewport across all frames for easy conversion into GIFs or videos.

### Technical Implementation Note
The layout engine uses a **non-local coordinate assignment**:
1. It assigns $x$-coordinates to leaf nodes first.
2. Parent nodes are then positioned at the **mean $x$** of their children, creating a clean, symmetrical branching aesthetic.

### How to use?

from bnbvisual import generate_tree_layout, draw_bnb_incremental
```python
from bnbvisual import generate_tree_layout, draw_bnb_incremental

# ... define your nodes and edges ...

# Calculate layout and dynamic canvas width
nodes, tree_width = generate_tree_layout(raw_nodes, edges)
canvas_width = max(10, tree_width * 1.05) 

# Generate the visualization
draw_bnb_incremental(nodes, edges, reveal_sequence, "output_prefix", figsize=(canvas_width, 8))
```
