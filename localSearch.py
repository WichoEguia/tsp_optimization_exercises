from Node import Node
from Timer import Timer
from random import randint as rand
import time

class localSearch():
    def __init__(self, tour):
        self.tour = tour
        self.localSearchSolution()

    def localSearchSolution(self):
        count = 0
        minSolution = self.tour
        start = time.time()
        
        # Loop that take count of the oportunities to minimize the solution
        while True:
            # Get random indexes to swap
            index_i = rand(2, len(minSolution) - 2)
            while True:
                index_j = rand(2, len(minSolution) - 2)
                if index_j != index_i:
                    break

            # Swap the indexes and get a posible solution
            posibleNeighbor = self.swap(index_i, index_j, minSolution)
            # print(time.time() - start)

            # Verify if the distance of the mi solution is shorter than the posible solution
            if self.distancePath(posibleNeighbor) < self.distancePath(minSolution):
                minSolution = posibleNeighbor
                count = 0
            else:
                count += 1

            # Out of loop if we dont have better result
            if count > 3000 or (time.time() - start) > (60 * 5):
            # if (time.time() - start) > 30:
                break

        # Print the path
        path = '2nd path: '
        for i in range(0, len(minSolution)):
            if i == len(minSolution) - 1:
                path += minSolution[i].idx
            else:
                path += minSolution[i].idx + ' -> '
        
        # print(path)
        distance = self.distancePath(minSolution)
        print(f'Distance of route 2: {distance}')
        # print('Time: ' + str(time.time() - self.time) + ' sec.')

    # Swap the solution and return a new array
    def swap(self, i, j, solution):
        n_solution = solution[:]
        n_solution[i], n_solution[j] = n_solution[j], n_solution[i]
        return n_solution

    # Get the distance of the whole path
    def distancePath(self, tour):
        distance = 0
        for i in range(len(tour)):
            distance += int(tour[i].distance(tour[i + 1]))
            if i + 1 == len(tour) - 1:
                break
        return distance
