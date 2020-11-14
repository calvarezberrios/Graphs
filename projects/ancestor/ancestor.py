from collections import deque

def earliest_ancestor(ancestors, starting_node):
    
    graph = createGraph(ancestors)

    queue = deque()
    earliest_parent = -1

    queue.appendleft(starting_node)

    while len(queue) > 0:
        curr = queue.pop()
        
        if curr not in graph:
            continue

        earliest_parent = min(graph[curr])
        
        for p in graph[curr]:
            queue.appendleft(p)

        
        
    return earliest_parent
            
            


def createGraph(ancestors):
    graph = {}

    for edge in ancestors:
        parent, child = edge[0], edge[1]
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = { parent }

    return graph
        