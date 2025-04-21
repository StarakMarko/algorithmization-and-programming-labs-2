def lst_to_graph(lst):
    graph_dic = {}
    for i in lst:
        if i[0] not in graph_dic:
            graph_dic[i[0]] = [i[1]]
        else:
            graph_dic[i[0]].append(i[1])

    return graph_dic


def gas_supply(cities, gas_storages, lst):
    connections = lst_to_graph(lst)
    result = []

    def dfs(connections, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        if node in connections.keys():
            for child in connections[node]:
                if child not in visited:
                    dfs(connections, child, visited)
        return visited

    for gas_storage in gas_storages:
        lst_cities = list(set(cities) - dfs(connections, gas_storage))
        if lst_cities:
            result.append(
                [gas_storage, list(set(cities) - dfs(connections, gas_storage))]
            )
    return result


cities = ["Львів", "Стрий", "Долина", "Жовква"]
gas_storages = ["Сховище_1", "Сховище_2", "Сховище_3"]
lst = [
    ["Львів", "Стрий"],
    ["Долина", "Львів"],
    ["Сховище_1", "Сховище_2"],
    ["Сховище_2", "Долина"],
    ["Сховище_3", "Жовква"],
]
print(gas_supply(cities, gas_storages, lst))
