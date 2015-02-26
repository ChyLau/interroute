#def dijkstra(graph, source):
#    dist[source] = 0
#    prev[source] = undef
#
#    for vertex in graph:
#        if vertex != source:
#            dist[vertex] = float("inf")
#            prev[vertex] = None
#
#        q.append(vertex)
#
#    while len(q) != 0:
#        u = min_dist
#        q.remove(u)
#
#        for neighbor of u:
#            alt = dist[u] + length(u, v)
#            if alt < dist[neighbor]:
#                dist[neighbor] = alt
#                prev[neighbor] = u
#
#    return dist[], prev[]

def dijkstra(net, s, t):
    # sanity check
    if s == t:
        print "The start and terminal nodes are the same. Minimum distance is 0."
    if net.has_key(s)==False:
        print "There is no start node called " + str(s) + "."
    if net.has_key(t)==False:
        print "There is no terminal node called " + str(t) + "."
    # create a labels dictionary
    labels={}
    # record whether a label was updated
    order={}
    # populate an initial labels dictionary
    for i in net.keys():
        if i == s: labels[i] = 0 # shortest distance form s to s is 0
        else: labels[i] = float("inf") # initial labels are infinity
    from copy import copy
    drop1 = copy(labels) # used for looping
    ## begin algorithm
    while len(drop1) > 0:
        # find the key with the lowest label
        minNode = min(drop1, key = drop1.get) #minNode is the node with the smallest label
        # update labels for nodes that are connected to minNode
        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        del drop1[minNode] # once a node has been visited, it's excluded from drop1
    ## end algorithm
    # print shortest path
    temp = copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if order.has_key(temp): temp = order[temp]
        else: print "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath)-1,-1,-1):
        path.append(rpath[j])
    print "The shortest path from " + s + " to " + t + " is " + str(path) + ". Minimum distance is " + str(labels[t]) + "."

# Given a large random network find the shortest path from '0' to '5'
#print dijkstra(net=randNet(), s='0', t='5')
