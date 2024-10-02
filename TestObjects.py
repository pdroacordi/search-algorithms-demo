from entities.Graph import Graph
from searches.AStar import AStar
from searches.Greedy import Greedy

graph = Graph()

greedy_search = Greedy(graph.bucharest)
greedy_search.search(graph.arad)


#astar_search = AStar(graph.bucharest)
#astar_search.search(graph.arad)

