"""
Command: py TSP-greedy_nearest_neighbor.py file iterations kmeans
"""

from Node import Node
from TspPath import Path
from sys import argv
from Timer import Timer
import random
from operator import itemgetter
from localSearch_firstIncome import localSearch

class NearestNeighbor():
    def __init__(self):
        self.nodes = self.getNodes()
        self.tour = []

    """
    description: Get the set of nodes from the file pased
    return: the set of all the nodes
    """
    def getNodes(self):
        rfile = open(argv[1], 'r')
        nodes = []

        for line in rfile:
            coordinates = self.getCoordinates(line)
            nodes.append(Node(coordinates))

        return nodes

    """
    description: Read each line and get the data of each node
    params: line, The current line of the file
    return: list with the idx, and cordinates of each node
    """
    def getCoordinates(self, line):
        data = line.split()
        
        if len(data) == 3:
            try:
                coordinates = (str(data[0]), float(data[1]), float(data[2]))
                return coordinates
            except ValueError:
                pass

        return None

    """
    description: Run the algorithm and get the tour
    return: tour of nodes
    """
    def run(self):
        current = self.nodes[0]

        while len(self.nodes) != len(self.tour):
            self.tour.append(current)
            arr_nodes = []

            for node in self.nodes:
                if node not in self.tour:
                    distance = current.distance(node)

                    arr_nodes.append({
                        'distance': distance,
                        'node': node
                    })

            if len(arr_nodes) > 0:
                current = self.getKmeanNode(arr_nodes)
                # break
            else:
                break

        self.tour.append(self.tour[0])
        return self.tour

    """
    description: select randomly a node
    return: selected node
    """
    def getKmeanNode(self, arr_opts):
        arr_opts = sorted(arr_opts, key=itemgetter('distance'))
        # print(arr_opts)
        kmeans = int(argv[3])
        arr_kmeans = []
        counter = 0

        for i in range(0, len(arr_opts)):
            if counter < kmeans:
                # print(str(i) + ' < ' + str(kmeans))
                arr_kmeans.append(arr_opts[i])
                counter += 1
        

        # random.seed(2000)
        index_rdm = random.randint(0, len(arr_kmeans) - 1)
        # print(f'index: {index_rdm}')
        # print(arr_kmeans)
        selected = arr_kmeans[index_rdm]

        # print(f'distance: {selected["distance"]}')
        # print(f'node: {selected["node"]}')
        # print('-----------------------------')

        return selected['node']

    """
    description: Calculate the distance in a array of nodes
    return: integer, distance
    """
    def distanceTour(self, path=None):
        distance = 0

        if path == None:
            path = self.tour

        for i in range(len(path)):
            distance += int(path[i].distance(path[i + 1]))
            if i + 1 == len(path) - 1:
                break

        return distance

    """
    description: Maxe a string with all nodes on the route
    return: String tour
    """
    def resultPath(self, path=None):
        result_path = ''

        if path == None:
            path = self.tour

        for i in range(0, len(path)):
            if i == len(path) - 1:
                result_path += path[i].idx
            else:
                result_path += path[i].idx + ' -> '

        return result_path

def main():
    min_distance = 10000000000
    
    if int(argv[2]) == 0:
        argv[2] = 1

    for i in range(0, int(argv[2])):
        print(f'iteration: {i}')
        nearest_neighbor = NearestNeighbor()
        tour = nearest_neighbor.run()

        # print(nearest_neighbor.resultPath(tour))
        print(f'Nearest Neighbor: {nearest_neighbor.distanceTour(tour)}')

        local_search = localSearch(tour)
        neighbor_tour = local_search.firstIncome()

        print(f'LS: {nearest_neighbor.distanceTour(neighbor_tour)}')
        print('******************************************')

        distance = local_search.distanceTour(neighbor_tour)
        if distance < min_distance:
            min_distance = distance
            min_tour = local_search.resultPath(neighbor_tour)
        
    # nearset_neighbor = NearestNeighbor()
    # min_tour = nearset_neighbor.resultPath(nearset_neighbor.run())
    # min_distance = nearset_neighbor.distanceTour(nearset_neighbor.run())

    print('----- Final Result -----')
    print(min_tour)
    print(min_distance)

if __name__ == '__main__':
    main()
