from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    _, costs = nx.dijkstra_predecessor_and_distance(g, starting_node)
    for node in g.nodes:
        if node not in costs:
            costs[node] = float("inf")

    return costs


if __name__ == '__main__':
    ...  # TODO записать граф
    graph = nx.DiGraph()
    graph.add_nodes_from('ABCDEFG')
    graph.add_weighted_edges_from([('A', 'B', 1), ('B', 'C', 3),
                                   ('C', 'E', 4), ('B', 'D', 2),
                                   ('C', 'D', 1), ('E', 'F', 3),
                                   ('D', 'A', 2), ('D', 'E', 2),
                                   ('G', 'D', 1)])
    nx.draw_networkx(graph)
    plt.show()
    print(dijkstra_algo(graph, 'G'))
