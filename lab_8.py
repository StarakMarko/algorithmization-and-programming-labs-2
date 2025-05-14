def read_roads_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    farms = [x.strip() for x in lines[0].split(",")]
    stores = [x.strip() for x in lines[1].split(",")]
    raw_edges = [line.split(",") for line in lines[2:]]
    edges = [(a.strip(), b.strip(), int(c.strip())) for a, b, c in raw_edges]
    return farms, stores, edges


def create_graph(graph, u, v, capacity):
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    if v not in graph[u]:
        graph[u][v] = 0
    if u not in graph[v]:
        graph[v][u] = 0
    graph[u][v] += capacity


def dfs(graph, u, sink, flow, visited):
    if u == sink:
        return flow
    visited[u] = True
    for v in graph[u]:
        if v not in visited and graph[u][v] > 0:
            if flow > graph[u][v]:
                min_cap = graph[u][v]
            else:
                min_cap = flow
            result = dfs(graph, v, sink, min_cap, visited)
            if result > 0:
                graph[u][v] -= result
                graph[v][u] += result
                return result
    return 0


def ford_fulkerson(file_path):
    farms, stores, edges = read_roads_csv(file_path)
    graph = {}

    for u, v, cap in edges:
        create_graph(graph, u, v, cap)

    source = "Source"
    sink = "Sink"
    for farm in farms:
        create_graph(graph, source, farm, float("inf"))
    for store in stores:
        create_graph(graph, store, sink, float("inf"))

    max_flow = 0
    while True:
        visited = {}
        flow = dfs(graph, source, sink, float("inf"), visited)
        if flow == 0:
            break
        max_flow += flow
    return max_flow


result = ford_fulkerson("roads.csv")
print(result)
