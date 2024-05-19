from collections import defaultdict, deque
import itertools
import sys


def parse_input():
    routes = []
    current_route = []
    for line in sys.stdin:
        line = line.strip()
        if line == 'deadend':
            if current_route:
                routes.append(current_route)
                current_route = []
        else:
            current_route.append(line)
    return routes


def create_graph(route):
    graph = defaultdict(dict)
    for street in route:
        start, end = street[0], street[-1]
        length = len(street)
        graph[start][end] = length
        graph[end][start] = length
    return graph


def floyd_warshall(graph, nodes):
    dist = {node: {node2: float('inf') for node2 in nodes} for node in nodes}
    for node in nodes:
        dist[node][node] = 0
    for node in graph:
        for neighbor in graph[node]:
            dist[node][neighbor] = graph[node][neighbor]
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def find_odd_degree_nodes(graph):
    degree = defaultdict(int)
    for node in graph:
        degree[node] = len(graph[node])
    return [node for node in degree if degree[node] % 2 == 1]


def min_cost_matching(odd_nodes, dist):
    min_cost = float('inf')
    best_matching = None
    for matching in itertools.permutations(odd_nodes):
        cost = sum(dist[matching[i]][matching[i+1]]
                   for i in range(0, len(odd_nodes), 2))
        if cost < min_cost:
            min_cost = cost
            best_matching = matching
    return min_cost


def chinese_postman_cost(graph):
    nodes = set(graph.keys())
    for node in graph:
        nodes.update(graph[node].keys())
    nodes = list(nodes)
    dist = floyd_warshall(graph, nodes)
    odd_nodes = find_odd_degree_nodes(graph)
    if not odd_nodes:
        return sum(graph[node][neighbor] for node in graph for neighbor in graph[node]) // 2
    min_cost = min_cost_matching(odd_nodes, dist)
    return sum(graph[node][neighbor] for node in graph for neighbor in graph[node]) // 2 + min_cost


def solve_cpp():
    routes = parse_input()
    results = []
    for route in routes:
        graph = create_graph(route)
        cost = chinese_postman_cost(graph)
        results.append(cost)
    for result in results:
        print(result)


if __name__ == "__main__":
    solve_cpp()
