from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs_1(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited = {node: False for node in g.nodes}
    q = deque()
    path = []

    visited[start_node] = True
    q.append(start_node)

    while q:
        current_node = q.pop()
        path.append(current_node)
        for neighbor in g[current_node]:  # g[current_node] - смежные узлы
            if not visited[neighbor]:
                q.append(neighbor)  # поджигаем узел графа
                visited[neighbor] = True  # если узел "подожжен", то мы его посещали

    return path

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited = {node: False for node in g.nodes}
    q = deque()
    path = []



    def recursion_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)


        for neighbor in g[current_node]:
            if not visited[neighbor]:
                recursion_dfs(neighbor)

    recursion_dfs(start_node)

    return path

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from('ABCDEFG')
    graph.add_edges_from([
        ('A', 'B'), ('A', 'C'),
        ('C', 'F'), ('E', 'G'),
        ('B', 'E'), ('B', 'D')
    ])
    nx.draw(graph)
    plt.show()
    print(dfs(graph,'A'))