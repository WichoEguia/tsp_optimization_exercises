from Node import Node

from sys import argv
import operator
from Timer import Timer
from localSearch import localSearch

# Global variable to save the distance
current_distance = 0

def insretPosition(node, tour):
    arr_distances = [
        # {
        #     distance
        #     index
        # }
    ]

    for i in range(len(tour)):
        a = tour[i].distance(node)
        b = tour[0].distance(node) if i == len(tour) - 1 else tour[i + 1].distance(node)
        c = tour[0].distance(tour[i]) if i == len(tour) - 1 else tour[i + 1].distance(tour[i])
        arr_distances.append({
            'distance': a + b - c,
            'index': i + 1 if i + 1 < len(tour) else 0
        })

    arr_distances.sort(key=operator.itemgetter('distance'))
    idx = arr_distances[0]['index']

    if idx == 0:
        tour.append(node)
    else:
        tour.insert(idx, node)

def nearest_neigbor(node, tour, nodes):
    global current_distance

    if len(tour) <= 2:
        # Put current node in a subtour
        tour.append(node)
    else:
        insretPosition(node, tour)

    min_distance = 100000
    min_node = None

    for k in range(len(nodes)):
        if nodes[k] not in tour:
            # Get the euclidean distance in current node and another one
            distance = node.distance(nodes[k])

            # Get the minimum distance an save the node
            if distance < min_distance:
                min_distance = distance
                min_node = nodes[k]
        else:
            continue
    
    # Validation to exit of the recursivity
    if len(nodes) != len(tour):
        # Update the distance
        current_distance += min_distance
        # Call the recursive function again
        nearest_neigbor(min_node, tour, nodes)
    else:
        # Update the distance with the distance inner the last and first node
        current_distance += tour[len(tour) - 1].distance(tour[0])
        # Add the first node at the end of tour
        tour.append(tour[0])

def distancePath(tour):
    distance = 0
    for i in range(len(tour)):
        distance += int(tour[i].distance(tour[i + 1]))
        if i + 1 == len(tour) - 1:
            break
    return distance

def getCoordinates(line):
	data = line.split()
	if len(data) == 3:
		try:
            # Get the cordinates to 
			coordinates = (str(data[0]), float(data[1]), float(data[2]))
			return coordinates
		except ValueError:
			pass
	return None

if __name__ == '__main__':
    # Init the cronometer
    # start_time = time.time()
    timer = Timer()
    timer.start()

    if len(argv) == 1:
        # Verify that file exists
        print("Error - File don't exists")
    elif argv[1][-4:] != ".txt":
        # Verify the file extension
        print("Error - The file must have the extension \'.txt\'")
    else:
        tour = []
        # The nodes array will save all the nodes
        nodes = []
        rfile = open(argv[1], 'r')

        # Get cordinates of each point and create a object of type Node
        for line in rfile:
            coordinates = getCoordinates(line)
            nodes.append(Node(coordinates))

        # Make a feasible tour with a recursive function
        nearest_neigbor(nodes[0], tour, nodes)
        
        # Print the results
        resultPath = '1st Path: '
        for i in range(0, len(tour)):
            if i == len(tour) - 1:
                resultPath += tour[i].idx
            else:
                resultPath += tour[i].idx + ' -> '
            
        print(resultPath)
        print('Distance of route 1: ' + str(distancePath(tour)))
        print(timer.elapsed('Time: '))
        print('-------------------------------------------')
        localSearch(tour)
        print(timer.elapsed('Time: '))
