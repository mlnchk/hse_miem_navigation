import json


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


def path_finder(start, end):
    graph = {
        'LW3': {'301', '325', 'LW4'},
        'LN3': {'307', '308', '317', 'LN4'},
        'LS3': {'Lu3', '317', '308', 'LS4'},
        'LE3': {'312', '313', 'LE4'},
        'Lu3': {'LS3', '315', '308', 'Lu4'},
        'WC3': {'317', '321'},
        '301': {'LW3', '302', '325'},
        '302': {'301', '303', '325'},
        '303': {'302', '304', '324'},
        '304': {'303', '305', '323'},
        '305': {'304', '306', '321'},
        '306': {'305', '307', 'WC3'},
        '307': {'306', 'LN3', 'WC3'},
        '308': {'LN3', '309', 'LS3', 'Lu3'},
        '309': {'308', '310', '315'},
        '310': {'309', '311', '314'},
        '311': {'310', '312', '314'},
        '312': {'311', 'LE3'},
        '313': {'314', 'LE3'},
        '315': {'Lu3', '309'},
        '314': {'313', '315', '310', '311'},
        '317': {'LS3', 'LN3', 'WC3'},
        '321': {'WC3', '305', '323'},
        '323': {'321', '305', '324'},
        '324': {'323', '325', '303'},
        '325': {'324', '302', 'LW3'},
        'LW4': {'401', '425', 'LW3'},
        'LN4': {'407', '408', '417', 'LN3'},
        'LS4': {'Lu4', '417', '408', 'LS3'},
        'LE4': {'412', '413', 'LE3'},
        'Lu4': {'LS4', '415', '408', 'Lu3'},
        'WC4': {'417', '421'},
        '401': {'LW4', '402', '425'},
        '402': {'401', '403', '425'},
        '403': {'402', '404', '424'},
        '404': {'403', '405', '423'},
        '405': {'404', '406', '421'},
        '406': {'405', '407', 'WC4'},
        '407': {'406', 'LN4', 'WC4'},
        '408': {'LN4', '409', 'LS4', 'Lu4'},
        '409': {'408', '410', '415'},
        '410': {'409', '411', '414'},
        '411': {'410', '412', '414'},
        '412': {'411', 'LE4'},
        '413': {'414', 'LE4'},
        '415': {'Lu4', '409'},
        '414': {'413', '415', '410', '411'},
        '417': {'LS4', 'LN4', 'WC4'},
        '421': {'WC4', '405', '423'},
        '423': {'421', '405', '424'},
        '424': {'423', '425', '403'},
        '425': {'424', '402', 'LW4'}
    }

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
