
def dfs(graph, start, visited):
    stack = [start]
    component = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            stack.extend(graph[vertex])

    return component

def find_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = dfs(graph, vertex, visited)
            components.append(sorted(component))

    return components


    return components

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4],
        6: [7],
        7: [6],
        8: []
    }

    components = find_connected_components(graph)
    print("Компоненты связности:", components)
