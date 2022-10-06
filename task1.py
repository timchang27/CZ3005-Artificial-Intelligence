from queue import PriorityQueue
from timeit import default_timer


def UCS_r(G, dist, start, end):
    total_nodes = len(G)
    pi = [None]*(total_nodes)
    visited = [0]*(total_nodes)
    expanded_nodes = 0
    key_list = list(G)

    # initialise the priority queue
    pq = PriorityQueue()

    start_timer = default_timer()

    # push first node into the queue
    pq.put((0, key_list[int(start)-1], None))

    while (pq):
        distance, u, previous_node = pq.get()
        index_u = int(u)-1

        # If source node
        if visited[index_u] == 1:
            continue
        expanded_nodes += 1

        # If destination node
        if u == end:
            pi[index_u] = previous_node
            stop_timer = default_timer()
            time_taken = stop_timer-start_timer

            return pi, expanded_nodes
        # For nodes in between
        pi[index_u] = previous_node
        visited[index_u] = 1
        for next_node in G[u]:
            key = u + "," + next_node
            if visited[int(next_node)-1] != 1:
                total_dist = distance + dist[key]
                pq.put((total_dist, next_node, u))

    stop_timer = default_timer()
    time_taken = stop_timer - start_timer
    return pi, expanded_nodes
