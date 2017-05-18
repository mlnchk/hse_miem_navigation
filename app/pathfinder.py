import json


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


def path_finder(start, end):
    all_ways = list(dfs_paths(graph, start, end))
    minimum = len(all_ways[0])
    for i in all_ways:
        if len(i) < minimum:
            minimum = len(i)
            min_item = i
    return min_item


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

# print(shortest_path(graph, '301', '408'))
# file = open('app/graph.json', 'r')
# graph = json.load(file)


# print(graph)
# k = 0
# for i in graph:
#     for j in graph:
#         if i != j and i != '311':
#             # print(k)
#             print(i, j)
#             print(shortest_path(graph, i, j))
#             k += 1

# print(k)
# print(shortest_path(graph, 'center', '207'))

# tmp = '301'
# if tmp in graph:
#     print('yes')