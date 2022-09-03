from typing import List
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


def add_rb_node(g: nx.Graph, values: List[str], color_map: List[str]):
    value = int(values[0])
    g.add_node(value, color=values[1])
    color_map.append(values[1])
    if len(values) == 3:
        g.add_edge(int(values[2]), value)


def add_avl_node(g: nx.Graph, values: List[str], color_map: List[str]):
    value = int(values[0])
    g.add_node(value)
    color_map.append('blue')
    if len(values) == 3:
        g.add_edge(int(values[2]), value)


def draw(tree_type: str):
    gr_tree = nx.Graph()
    color_map = []
    add_node = add_avl_node if tree_type == 'AVL' else add_rb_node
    while True:
        try:
            input_buf = input()
        except EOFError:
            break

        if input_buf == '':
            tree_pos = graphviz_layout(gr_tree, "dot")
            nx.draw(gr_tree, tree_pos, with_labels=True,
                    node_color=color_map, font_color="white")
            plt.show(block=True)
            continue

        if input_buf in ('AVL', 'RB'):
            if input_buf != tree_type:
                draw(input_buf)
                break

        if input_buf == tree_type:
            gr_tree.clear()
            color_map.clear()
        else:
            input_values = input_buf.split(' ')
            add_node(gr_tree, input_values, color_map)


if (__name__ == '__main__'):
    tree_type_str = input()
    while tree_type_str == '':
        tree_type_str = input()
    if (tree_type_str not in ['AVL', 'RB']):
        raise (ValueError())
    draw(tree_type_str)
