#
# topological sort
# https://www.algotree.org/algorithms/tree_graph_traversal/lexical_topological_sort_python/
#

graph = {
# node: [before nodes]
    1: [0, 2, 3],
    3: [0, 2],
    4: [0, 3]
}

print(f'graph: {graph}')

# incoming (node) edge counts
edges_count = {}

# keys printed in order
for key in range(5):
    edges_count[key] = 0
for key in graph.keys():
    edges_count[key] = 0
for key in [item for items in graph.values() for item in items]:
    edges_count[key] = 0

for key, value in graph.items():
    for value2 in value:
        edges_count[value2] += 1

print(f'edges_count: {edges_count}')

# node is free if it's edge count is zero
def get_free_nodes():
    global edges_count
    free_nodes = []
    for k, v in edges_count.items():
        if v == 0:
            free_nodes.append(k)
    return sorted(free_nodes) # ordering happens here!

# remove node from graph:
# 1) remove all nodes with zero edges
# 2) remove the node from graph
# 3) decrease edge counts
def remove_from_graph(node):
    global edges_count
    for k, v in list(edges_count.items()):
        if v == 0:
            del edges_count[k]
    global graph
    edge_nodes = graph.pop(node, None)
    if not (edge_nodes is None):
        for x in edge_nodes:
            edges_count[x] -= 1

sorted_nodes = []
next_nodes = []

while len(edges_count) > 0 or len(next_nodes) > 0:
    print('---')

    # nodes that are free to be processed are those
    # without incoming edges in lexical order
    next_nodes.extend(get_free_nodes())
    print(f'next_nodes: {next_nodes}')

    # this is the next node to be processed
    resolve_node = next_nodes.pop(0)
    print(f'resolve_node: {resolve_node}')

    # remove the node from the graph and edges count
    remove_from_graph(resolve_node)
    print(f'graph: {graph}')
    print(f'edges_count: {edges_count}')

    # add the node to the sorted nodes
    sorted_nodes.append(resolve_node)
    print(f'sorted_nodes: {sorted_nodes}')
