from math import sqrt, pow
from queue import PriorityQueue


def AStar(graph, dist, cost, coord, start, end, budget):
    # Initialise Priority Queue
    pq = PriorityQueue()
    # Priority in pq, distance to node, cost of node, node index, list of nodes in path
    pq.put((0, 0, 0, start, []))

    # Dictionary to store lowest costs and cur_dists
    min_cost = {key: float("inf") for key in coord}
    min_dist = {key: float("inf") for key in coord}

    while not pq.empty():
        priority, node_dist, node_cost, node, cur_path = pq.get()

        if node == end:
            return cur_path, node_dist, node_cost

        for adj_node in graph[node]:
            cur_dist = node_dist + dist[get_distkey(node, adj_node)]
            total_cost = node_cost + cost[get_distkey(node, adj_node)]

            # Skip node if total cost exceeds energy budget
            if total_cost > budget:
                continue

            if cur_dist < min_dist[adj_node] or total_cost < min_cost[adj_node]:
                min_dist[adj_node] = cur_dist
                min_cost[adj_node] = total_cost
                # New shortest distance as prio
                new_priority = cur_dist + get_heuristic(adj_node, end, coord)
                # Add adjacent node to the new list
                new_path = cur_path.copy()
                new_path.append(adj_node)
                pq.put((new_priority, cur_dist, total_cost, adj_node, new_path))


def get_distkey(node1, node2):
    return node1 + ',' + node2  # "1,2"


def get_heuristic(cur, dest, coord):
    # Approxmination - Calculate Euclidean cur_dist for cur and dest
    cur_x, cur_y = coord[cur]
    dest_x, dest_y = coord[dest]
    dist = sqrt(pow((dest_x-cur_x), 2) + pow((dest_y-cur_y), 2))
    return dist
