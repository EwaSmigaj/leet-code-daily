import sys
from typing import List


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    graph = initiate_graph(edges,n)
    nodes_zero = []
    for node, val in graph.items():
        if val == {}:
            nodes_zero.append(node)
    if len(nodes_zero) > 0:
        return max(nodes_zero)

    result_city = -1
    smallest_connection_val = -1

    for i in range(n):
        if graph[i] != {}:
            costs = dijkstra(i, graph)

        accepted_costs = {}
        for node in costs.keys():
            if costs[node] <= distanceThreshold:
                accepted_costs[node] = costs[node]
        if len(accepted_costs.keys()) <= smallest_connection_val or result_city == -1:
            result_city = i
            smallest_connection_val = len(accepted_costs.keys())
    print(result_city)
    return result_city


def dijkstra(startingNode, graph):
    not_visited = []
    visited = []
    routes_info = {}
    for node in graph.keys():
        if node != startingNode:
            not_visited.append(node)
            routes_info[node] = [sys.maxsize, -1]
        else:
            not_visited.append(node)
            routes_info[node] = [0, -1]
    # print(routes_info)

    #find out which node we will calculate
    while len(not_visited) >= 1:
        shortest_path = sys.maxsize
        node_to_pick = -1
        for element in routes_info.keys():
            if element not in visited:
                if routes_info[element][0] < shortest_path:
                    shortest_path = routes_info[element][0]
                    node_to_pick = element

        #find unwisited neighbours
        dict_of_nodes_connections = graph[node_to_pick]
        print("analysing_neighbours of= " + str(node_to_pick))
        for i in dict_of_nodes_connections.keys():
            print("i = " + str(i))
            if i not in visited:
                print(routes_info)
                if routes_info[node_to_pick][0] + dict_of_nodes_connections[i] < routes_info[i][0]:
                    routes_info[i] = [dict_of_nodes_connections[i], node_to_pick]
        visited.append(node_to_pick)
        not_visited.pop(not_visited.index(node_to_pick))


    #calculate final cost
    final_costs = {}
    for node in routes_info.keys():
        if node != startingNode:
            # print(node)
            final_costs[node] = routes_info[node][0]
            # print(final_costs)
            tmpNode = routes_info[node][1]
            # print(tmpNode)
            while tmpNode != startingNode:
                final_costs[node] += routes_info[tmpNode][0]
                tmpNode = routes_info[tmpNode][1]
    return final_costs


def initiate_graph(edges, n):
    graph = {}
    for i in range(n):
        graph[i] = {}

    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph




n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

findTheCity(n, edges, distanceThreshold)
