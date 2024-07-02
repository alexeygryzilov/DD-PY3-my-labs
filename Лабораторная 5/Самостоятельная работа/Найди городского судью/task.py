from typing import List
import networkx as nx
import matplotlib.pyplot as plt


def find_judge(n: int, trust: List[List[int]]) -> int:

    if n < 2:
        return -1
    confidants = set()
    for person in trust:
        confidants.add(person[1])

    if len(confidants) == 1:
        return person[1]
    return -1

if __name__ == '__main__':

    print(find_judge(3,[[1,3],[2,3],[3,1]]))
