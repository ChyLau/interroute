import networkx as nx
import matplotlib.pyplot as plt


def drawMap():
    graph = nx.Graph()

    #graph.add_node(10)
    #graph.add_nodes_from([2,3])

    graph.add_edges_from([(1,2),(1,3)])

    nx.draw(graph)
    plt.show()


if __name__ == "__main__":
    drawMap()
