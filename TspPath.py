import numpy as np
import matplotlib.pyplot as plt
from Node import Node

class Path:
    def __init__(self, nodes):
        self.arr_nodes = []

        for node in nodes:
            self.arr_nodes.append([node.x, node.y])
        
        self.drawPath()

    def drawPath(self):
        data = np.array(self.arr_nodes)
        plt.plot(*data.T)
        plt.show()
