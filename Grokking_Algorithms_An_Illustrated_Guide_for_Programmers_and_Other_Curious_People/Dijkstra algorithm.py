graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
cost = {'a': 6, 'b': 2, 'fin': infinity}
parent = {'a': 'start', 'b': 'start', 'fin': None}

processed = []


def find_lowest_cost_node(cost_input):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in cost_input:
        cost = cost_input[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, cost, parent):
    node = find_lowest_cost_node(cost)
    while node is not None:
        cost_value = cost[node]
        neighbor_node = graph[node]
        for i in neighbor_node.keys():
            new_cost = cost_value + neighbor_node[i]
            if cost[i] > new_cost:
                cost[i] = new_cost
                parent[i] = node
        processed.append(node)
        node = find_lowest_cost_node(cost)

    path = ['fin']

    def route(input='fin'):
        if input == 'start':
            return ['start']
        else:
            add = parent[input]
            path.insert(0, add)
        return route(add)

    route()
    return path


dijkstra(graph, cost, parent)