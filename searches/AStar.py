import numpy as np

from entities import Vertex


class OrderedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def insert(self, vertex: Vertex):
        if self.last_position == self.capacity - 1:
            print('Capacidade máxima atingida.')
            return
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].distance_astar > vertex.distance_astar:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = vertex
        self.last_position += 1

    def print(self):
        if self.last_position == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i].vertex.label, ' - ',
                      self.values[i].cost, ' - ',
                      self.values[i].vertex.distance_to_destination, ' - ',
                      self.values[i].distance_astar)

class AStar:
    def __init__(self, target):
        self.target = target
        self.found = False

    def search(self, current: Vertex):
        print('-------')
        print('Atual: {}'.format(current.label))
        current.visited = True

        if current == self.target:
            self.found = True
        else:
            orderedArray = OrderedArray(len(current.adjacent))
            for adjacent in current.adjacent:
                if adjacent.vertex.visited == False:
                    adjacent.vertex.visited = True
                    orderedArray.insert(adjacent)
            orderedArray.print()
            if orderedArray.values[0] != None:
                self.search(orderedArray.values[0].vertex)


