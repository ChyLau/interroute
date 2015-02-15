def dijkstra(graph, source):
    dist[source] = 0
    prev[source] = undef

    for vertex in graph:
        if vertex != source:
            dist[vertex] = float("inf")
            prev[vertex] = None

        q.append(vertex)

    while len(q) != 0:
        u = min_dist
        q.remove(u)

        for neighbor of u:
            alt = dist[u] + length(u, v)
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u

    return dist[], prev[]
