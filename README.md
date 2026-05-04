---
# Dynamic Branch and Bound Tree Visualizer

<img width="9872" height="1691" alt="bnb_massive_depth_11" src="https://github.com/user-attachments/assets/1d78119a-260c-4ee7-9291-8c3904ff3a30" />
<img width="3356" height="1277" alt="bnb_ex4_11" src="https://github.com/user-attachments/assets/9f1b3285-e18c-420b-8429-d39ada3ac041" />



A Python utility for generating incremental, publication-quality visualizations of **Branch and Bound** search trees. This tool calculates optimal tree layouts and generates step-by-step frames showing the evolution of the optimization process, including node status changes (e.g., fractional, pruned, incumbent).

### Features

*   **Auto-Layout Engine:** Automatically calculates horizontal and vertical spacing based on text length to prevent overlapping nodes.
*   **Incremental Reveal:** Generates a sequence of images representing the "steps" of the algorithm.
*   **Status Tracking:** Nodes change colors based on their state (Root, Fractional, Incumbent, Pruned, Infeasible) at each specific step.
*   **Symmetrical Framing:** Maintains a consistent viewport across all frames for easy conversion into GIFs or videos.

### Technical Implementation Note
The layout engine uses a **non-local coordinate assignment**:
1. It assigns $x$-coordinates to leaf nodes first.
2. Parent nodes are then positioned at the **mean $x$** of their children, creating a clean, symmetrical branching aesthetic.

### How to use?
Refer to [this file](https://raw.githubusercontent.com/parinchaipunya/bnb-tree-visualization/refs/heads/main/example_deep.py) and [this file](https://raw.githubusercontent.com/parinchaipunya/bnb-tree-visualization/refs/heads/main/example_wide.py) for pretty complete examples.
