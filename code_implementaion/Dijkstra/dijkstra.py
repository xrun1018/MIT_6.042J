# @XuRUn: 04/2021

import numpy as np


def dijkstra(G, start, dest):
    """
    Dijkstra algorithm implementations

    G: A weighted matrix

    start: The start vertex

    dest: The destination vertex
    """
    labels = list()
    for i in range(G.shape[0]):
        labels.append(np.inf)
    labels[start] = 0
    S = list()

    while dest not in S:
        min_label = np.inf
        for i in range(G.shape[0]):
            if labels[i] < min_label and i not in S:
                min_label = labels[i]
                current = i

        S = S + [current]
        for i in range(G.shape[0]):
            if i not in S:
                if labels[current] + G[current, i] < labels[i]:
                    labels[i] = labels[current] + G[current, i]
    return (labels[dest], S)
