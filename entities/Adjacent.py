class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.distance_astar = vertex.distance_to_destination + self.cost