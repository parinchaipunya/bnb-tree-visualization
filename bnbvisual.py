import matplotlib.pyplot as plt


def generate_tree_layout(raw_nodes, edges, y_spacing=1.0):
    max_char_length = 0
    for data in raw_nodes.values():
        name = data[0]
        z = data[1]
        x_vals = data[2]

        # Simulate what the longest line of text will be
        z_str = f"Z={z:.2f}" if isinstance(z, (int, float)) else f"Z={z}"
        x_str = f"x̄=({', '.join([f'{v:.2f}' for v in x_vals])})" if x_vals else ""

        box_width_chars = max(len(name), len(z_str), len(x_str))
        if box_width_chars > max_char_length:
            max_char_length = box_width_chars

    auto_spacing = max(2.0, max_char_length * 0.18)

    children = {nid: [] for nid in raw_nodes.keys()}
    parents = {}

    for u, v, _ in edges:
        if u in children:
            children[u].append(v)
        parents[v] = u

    root = next(nid for nid in raw_nodes.keys() if nid not in parents)

    positions = {}
    current_leaf_x = 0

    def assign_coords(node_id, depth=0):
        nonlocal current_leaf_x

        if not children[node_id]:
            positions[node_id] = (current_leaf_x, -depth * y_spacing)
            current_leaf_x += auto_spacing
        else:
            child_xs = []
            for child_id in children[node_id]:
                assign_coords(child_id, depth + 1)
                child_xs.append(positions[child_id][0])

            avg_x = sum(child_xs) / len(child_xs)
            positions[node_id] = (avg_x, -depth * y_spacing)

    assign_coords(root)

    final_nodes = {}
    for nid, data in raw_nodes.items():
        final_nodes[nid] = (positions[nid], *data)

    return final_nodes, current_leaf_x


def draw_bnb_incremental(
    all_nodes,
    all_edges,
    reveal_order,
    filename,
    title_prefix="B&B Step",
    figsize=(10, 7),
    savepng=True,
    showplt=True,
):
    PALETTE = {
        "root": "lightgray",
        "explored": "lightgray",
        "fractional": "lightblue",
        "incumbent": "lightgreen",
        "pruned": "salmon",
        "infeasible": "salmon",
    }

    root_id = reveal_order[0][0]
    root_x = all_nodes[root_id][0][0]

    max_offset = 0
    for node_id in all_nodes:
        dist = abs(all_nodes[node_id][0][0] - root_x)
        if dist > max_offset:
            max_offset = dist

    x_padding = max_offset * 0.15 if max_offset > 0 else 0.5
    x_min = root_x - max_offset - x_padding
    x_max = root_x + max_offset + x_padding

    all_y = [data[0][1] for data in all_nodes.values()]
    y_padding = (max(all_y) - min(all_y)) * 0.15 if max(all_y) != min(all_y) else 0.5
    y_min, y_max = min(all_y) - y_padding, max(all_y) + y_padding

    visible_nodes = []

    for i, group in enumerate(reveal_order):
        visible_nodes.extend(group)

        currently_has_children = set()
        for u, v, _ in all_edges:
            if u in visible_nodes and v in visible_nodes:
                currently_has_children.add(u)

        fig, ax = plt.subplots(figsize=figsize)

        for u, v, branch_txt in all_edges:
            if u in visible_nodes and v in visible_nodes:
                (x0, y0) = all_nodes[u][0]
                (x1, y1) = all_nodes[v][0]
                ax.plot([x0, x1], [y0, y1], "k-", lw=1.5, alpha=0.6, zorder=1)

                mid_x, mid_y = (x0 + x1) / 2, (y0 + y1) / 2
                ax.text(
                    mid_x,
                    mid_y,
                    branch_txt,
                    fontsize=9,
                    ha="center",
                    va="center",
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.7),
                )

        for nid in visible_nodes:
            node_data = all_nodes[nid]
            pos, name, z, x_vals, status_history = node_data

            current_status = "root"
            for step_idx in sorted(status_history.keys()):
                if step_idx <= i:
                    current_status = status_history[step_idx]

            z_str = f"Z={z:.2f}" if isinstance(z, (int, float)) else f"Z={z}"
            x_str = f"\nx̄=({', '.join([f'{v:.2f}' for v in x_vals])})" if x_vals else ""

            if current_status.lower() == "infeasible":
                x_str = "\nx̄=N/A"

            full_label = f"{name}\n{z_str}{x_str}\n{current_status.capitalize()}"

            color = (
                "lightgray"
                if nid in currently_has_children
                else PALETTE.get(current_status.lower(), "white")
            )

            ax.text(
                pos[0],
                pos[1],
                full_label,
                ha="center",
                va="center",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.5", facecolor=color, edgecolor="black"),
                zorder=5,
            )

        ax.set_title(f"{title_prefix} {i + 1}", fontsize=14, fontweight="bold", pad=2)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.axis("off")

        plt.tight_layout()
        plt.subplots_adjust(top=0.92)
        if savepng:
            plt.savefig(f"{filename}_{i + 1}.png", bbox_inches="tight")
        if showplt:
            plt.show()
