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
        'LW': {'301', '325'},
        'LN': {'307', '308', '317'},
        'LS': {'317', 'lift', '308'},
        'LE': {'312', '313'},
        'lift': {'LS', '315', '308'},
        'WC': {'317', '321', '306', '307'},
        '301': {'LW', '302', '325'},
        '302': {'301', '303', '325'},
        '303': {'302', '304', '324'},
        '304': {'303', '305', '323'},
        '305': {'304', '306', '321'},
        '306': {'305', '307', 'WC'},
        '307': {'306', 'LN', 'WC'},
        '308': {'LN', '309', 'LS', 'lift'},
        '309': {'308', '310', '315'},
        '310': {'309', '311', '314'},
        '311': {'310', '312', '314'},
        '312': {'311', 'LE'},
        '313': {'314', 'LE'},
        '315': {'lift', '309'},
        '314': {'313', '315', '310', '311'},
        '317': {'LS', 'LN', 'WC'},
        '321': {'WC', '305', '323'},
        '323': {'321', '305', '324'},
        '324': {'323', '325', '303'},
        '325': {'324', '302', 'LW'}
    }

    # start, end = 'LW', '314'

    all_ways = list(dfs_paths(graph, start, end))
    minimum = len(all_ways[0])
    for i in all_ways:
        if len(i) < minimum:
            minimum = len(i)
            min_item = i
    return min_item
