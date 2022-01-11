# @XuRUn: 04/2021

from dijkstra import dijkstra
import numpy as np


def main():
    G = np.array([[0, 4, 2, np.inf, np.inf, np.inf],
                  [4, 0, 1, 5, np.inf, np.inf],
                  [2, 1, 0, 8, 10, np.inf],
                  [np.inf, 5, 8, 0, 2, 6],
                  [np.inf, np.inf, np.inf, 10, 2, 3],
                  [np.inf, np.inf, np.inf, 6, 3, 0]])

    print("S = ", dijkstra(G, 0, 5))
    # print(G.shape[0])


if __name__ == "__main__":
    main()
