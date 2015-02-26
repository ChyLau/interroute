import matplotlib.pyplot as plt
import dijkstra

def main():
	#def drawMap():
	#    graph = nx.Graph()
	#
	#    #graph.add_node(10)
	#    #graph.add_nodes_from([2,3])
	#
	#    graph.add_edges_from([(1,2),(1,3)])
	#
	#    nx.draw(graph)
	#    plt.show()
	
	net = {'0':{'1':100, '2':300},
	       '1':{'3':500, '4':500, '5':100},
	       '2':{'4':100, '5':100},
	       '3':{'5':20},
	       '4':{'5':20},
	       '5':{}
	       }
	
	dijkstra.dijkstra(net, '0', '5')


if __name__ == "__main__":                                                     
	main()
