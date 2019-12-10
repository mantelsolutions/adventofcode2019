import networkx as nx

# use directed graph
graph = nx.DiGraph()

lines = [line.strip() for line in open('day6/input.txt')]

for line in lines:
    nodeA, nodeB = line.split(')')
    graph.add_edge(nodeA, nodeB)

edges = list(nx.bfs_edges(graph,"COM"))
print(len(edges))

depthFirstSearch = list(nx.dfs_postorder_nodes(graph,"COM"))
print(depthFirstSearch)

totalOrbits = 0
nodeToOrbitsMap = {}
for node in depthFirstSearch:
    print(graph[node])
    nodeOrbits = 0
    for connectedNode in graph[node]:
        print(connectedNode)
        nodeOrbits += nodeToOrbitsMap[connectedNode] + 1
        print("Node " + connectedNode + " orbits: " + str(nodeOrbits))
    nodeToOrbitsMap[node] = nodeOrbits
    totalOrbits += nodeOrbits

print("Result part1: " + str(totalOrbits))

# undirected graph for shortest path
undirectedGraph = graph.to_undirected()
steps = nx.shortest_path_length(undirectedGraph,"YOU", "SAN")
resultPart2 = steps - 2 #remove you and san
print("Result part2: " + str(resultPart2))