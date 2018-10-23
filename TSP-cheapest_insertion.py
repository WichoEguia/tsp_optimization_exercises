from Node import Node
from TspPath import Path
from sys import argv
import operator
from Timer import Timer
from localSearch import localSearch

def calculaDistancia(tour):
    distance = 0
    for i in range(len(tour)):
        distance += tour[i].distance(tour[i + 1])
        if i + 1 == len(tour) - 1:
            break
    return distance

def findNode(idx, nodes):
    for node in nodes:
        if node.idx == idx:
            return node

def getCloserNode(nodes, tour):
    arr_distances = [
        # {
        #     distance: 0,
        #     node: node
        # }
    ]
    for node in tour:
        min_distance = 1000000
        min_node = None
        for i in range(len(nodes)):
            if nodes[i] not in tour:
                distance = node.distance(nodes[i])
                if distance < min_distance:
                    min_distance = distance
                    min_node = nodes[i].idx
            else:
                continue

        arr_distances.append({
            'distance': min_distance,
            'node': min_node
        })

    arr_distances.sort(key=operator.itemgetter('distance'))
    closestNodeData = arr_distances[0]

    return findNode(closestNodeData['node'], nodes)

def cheapestInsertion(nodes, tour):
    if len(tour) > 1:
        if len(tour) == 2:
            nextNode = getCloserNode(nodes, tour)
            tour.append(nextNode)
            cheapestInsertion(nodes, tour)
        elif len(tour) < len(nodes):
            nextNode = getCloserNode(nodes, tour)
            arr_distances = [
                # {
                #     distance
                #     index
                # }
            ]

            for i in range(len(tour)):
                a = tour[i].distance(nextNode)
                b = tour[0].distance(nextNode) if i == len(tour) - 1 else tour[i + 1].distance(nextNode)
                c = tour[0].distance(tour[i]) if i == len(tour) - 1 else tour[i + 1].distance(tour[i])
                arr_distances.append({
                    'distance': a + b - c,
                    'index': i + 1 if i + 1 < len(tour) else 0
                })
            
            arr_distances.sort(key=operator.itemgetter('distance'))
            idx = arr_distances[0]['index']

            if idx == 0:
                tour.append(nextNode)
            else:
                tour.insert(idx, nextNode)

            cheapestInsertion(nodes, tour)
    else:
        nextNode = getCloserNode(nodes, tour)
        tour.append(nextNode)
        cheapestInsertion(nodes, tour)

def getCoordinates(line):
	data = line.split()
	if len(data) == 3:
		try:
			coordinates = (str(data[0]), float(data[1]), float(data[2]))
			return coordinates
		except ValueError:
			pass
	return None

if __name__ == '__main__':
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
        nodes = []
        rfile = open(argv[1], 'r')

        for line in rfile:
            coordinates = getCoordinates(line)
            nodes.append(Node(coordinates))
        
        tour = [nodes[0]]
        cheapestInsertion(nodes, tour)
        tour.append(nodes[0])

        resultPath = '1st Path: '
        for node in tour:
            resultPath += node.idx + ' -> '

        print(resultPath)
        print('Distance of route: ' + str(calculaDistancia(tour)))
        # print('Time: ' + str(time.time() - start_time) + ' sec.')
        # Path(tour)
        print(timer.elapsed('Time: '))
        print('-------------------------------------------')
        localSearch(tour)
        print(timer.elapsed('Time: '))