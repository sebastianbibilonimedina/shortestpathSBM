from queue import PriorityQueue

def dijkstra(graph, start_vertex, end_vertex):
    if start_vertex not in graph:
        raise ValueError('Start vertex not in graph')
    if end_vertex not in graph:
        raise ValueError('End vertex not in graph')

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    previous_vertices = {vertex: None for vertex in graph}
    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        current_distance, current_vertex = pq.get()

        print(f"Exploring {current_vertex} at distance {current_distance}")

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            print(f"Checking neighbor {neighbor}: current {distances[neighbor]}, new {distance}")

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                pq.put((distance, neighbor))

    path = []
    step = end_vertex
    if distances[step] == float('infinity'):
        return (float('infinity'), [])  # Unreachable
    while step is not None:
        path.append(step)
        step = previous_vertices[step]

    path.reverse()

    return (distances[end_vertex], path)
