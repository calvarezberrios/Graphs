from collections import deque

def earliest_ancestor(ancestors, starting_node):
    
    graph = createGraph(ancestors)

    stack = deque()
    visited = set()

    stack = ancestors[0][0]

    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)

        



def createGraph(ancestors):
    graph = {}

    

    for edge in ancestors:
        parent, child = edge[0], edge[1]
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = { child }

    return graph
        