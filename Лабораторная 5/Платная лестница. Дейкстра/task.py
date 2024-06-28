from typing import Union, List

import networkx as nx
import matplotlib.pyplot as plt


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    path = nx.shortest_path(graph, source=0, target=len(graph.nodes) -1, weight="weight")


    return path
def make_list(stairway: List[int]):

    list_ = []

    for i in range(len(stairway)):
        stair = (i, i + 1, stairway[i])
        list_.append(stair)
        if not i + 2 > len(stairway):
            stair = (i, i + 2, stairway[i + 1])
            list_.append(stair)
    return list_

def make_graph(stairway: List[int]):

    graph = nx.DiGraph()
    list_ = make_list(stairway)
    graph.add_weighted_edges_from(list_)
    nx.draw(graph)
    plt.show()
    return graph



if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    list_ = make_list(stairway)
    stairway_graph = make_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
