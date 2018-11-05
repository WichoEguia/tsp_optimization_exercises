from Node import Node
from Timer import Timer
import random
import time

class localSearch():
    def __init__(self, tour):
        self.improved_solution = tour

    def firstIncome(self):
        count = 0
        start = time.time()
        random.seed(2000)
        
        while True:
            index_i = random.randint(2, len(self.improved_solution) - 2)
            while True:
                index_j = random.randint(2, len(self.improved_solution) - 2)
                if index_j != index_i:
                    break

            posibleNeighbor = self.swap(index_i, index_j, self.improved_solution)

            if self.distanceTour(posibleNeighbor) < self.distanceTour(self.improved_solution):
                self.improved_solution = posibleNeighbor
                count = 0
            else:
                count += 1

            # if (time.time() - start) > 30:
            if count > 3000 or (time.time() - start) > 120:
                break

        return self.improved_solution

    def distanceTour(self, path=None):
        distance = 0

        if path == None:
            path = self.improved_solution

        for i in range(len(path)):
            distance += int(path[i].distance(path[i + 1]))
            if i + 1 == len(path) - 1:
                break

        return distance

    def resultPath(self, path=None):
        result_path = ''

        if path == None:
            path = self.improved_solution

        for i in range(0, len(path)):
            if i == len(path) - 1:
                result_path += path[i].idx
            else:
                result_path += path[i].idx + ' -> '

        return result_path

    # Swap the solution and return a new array
    def swap(self, i, j, solution):
        n_solution = solution[:]
        n_solution[i], n_solution[j] = n_solution[j], n_solution[i]
        return n_solution
