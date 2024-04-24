from network_graph import create_network_graph
from network_graph_dijkstra import dijkstra
import networkx as nx


def main():
    start_vertex = input("Enter the start vertex: ")
    end_vertex = input("Enter the end vertex: ")

    networkx_graph = create_network_graph()

    distance, path = dijkstra(networkx_graph, start_vertex, end_vertex)

    print("Our Dijkstra:")
    print("Distance: ", distance)
    print("Path: ", path)

    nx_distance, nx_path = nx.single_source_dijkstra(networkx_graph, start_vertex, target=end_vertex)

    print("NetworkX Dijkstra:")
    print("Distance: ", nx_distance)
    print("Path: ", nx_path)

    print("Results are the same: ", distance == nx_distance and path == nx_path)


if __name__ == "__main__":
    main()