from entities.Adjacent import Adjacent


class Vertex:
    def __init__(self, label, distance_to_destination):
        self.label = label
        self.visited = False
        self.adjacent = []
        self.distance_to_destination = distance_to_destination

    def add_adjacent(self, vertex: Adjacent):
        self.adjacent.append(vertex)

    def show_adjacent(self):
        for i in self.adjacent:
            print(i.vertex.label, i.cost)