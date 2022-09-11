def solution(banana_list):

    if len(banana_list) == 1:

        return 1

    is_cyclic_graph = Graph(set(),set()) #Create a graph where if (u,v) is an edge, then there is a cycle between u and v.

    i = 0

    while i < len(banana_list) - 1:

        j = i+1

        while j < len(banana_list):

            is_cyclic_graph.addVertex(i) #If i is already in the graph, nothing happens, because the vertex are a set.
            is_cyclic_graph.addVertex(j)

            if isCyclic(banana_list[i],banana_list[j]):

                is_cyclic_graph.addEdge(i,j)

            j+=1

        i += 1

    if len(banana_list)%2 == 0:

        e = 0
    
    else:

        e = 1

    return len(banana_list) - maximumCardinalityMatching(is_cyclic_graph) + e #If the number of trainers odd, there's always at least one trainer that can't be distracted.


def isCyclic(x,y):
    '''
    Returns True if x, y will eventually go into a Cycle.
    '''
    if x==y:
        return False

    if x%2 != y%2: #Ex: x is even and y is odd and x>y. Then after the first iteration x 
                    #will be odd because (x-y) is odd, the same for y because odd + odd = even. So the loop will never end.
        return True #An analogous argument can be made in the case where y>x. Odd-even = odd and 2*even = even.

    s = x + y #In the case both numbers are even or odd, the sum will be even.

    while not s%2:

        s = s>>1 #Divide by 2 until the sum is odd.
                        #I recognized a pattern where if x is a multiple of s, after removing the 2's factors of s, eventually x==y.
    return (x % s)!=0  #A similar argument can be made using gcd.


class Graph: #Creates graph structure.

    def __init__(self, V, E):
        self.vertex = V
        self.edge = E
    
    def addEdge(self, u, v):
        self.edge.add((u,v))
        self.edge.add((v,u)) #Undirected graph

    def addVertex(self, v):
        self.vertex.add(v)

    def __str__(self): #Debugging purposes
        return "Vertex: " + str(self.vertex) + " Edge: " + str(self.edge)


def maximumCardinalityMatching(G):
    """
    Takes a graph as parameter and returns the maximum cardinality matching.
    That is, a matching where each vertex in V is incident with at most one edge in M and |M| is maximized. 
    Blosson Algorithm could also be used, but is harder to implement.
    """
    max_matching = 0

    j_vertex = [-1 for _ in range(len(G.vertex))] #The jVertex[i] is the vertex that is matched with i.

    for i in range(len(G.vertex)):

        visited = [False for _ in range(len(G.vertex))]

        is_N, j_vertex, visited = isNecesary(G, i, j_vertex, visited)

        if is_N:
                
            max_matching += 1

    return max_matching


def isNecesary(G, i, j_vertex, visited):
    """
    Returns True if the vertex i is necesary for the matching. Also return updated jVertex and visited. Greddy approach.
    """
    for v in range(len(G.vertex)):

        if (i,v) in G.edge and not visited[v]:

            visited[v] = True

            is_N, j_vertex, visited = isNecesary(G, j_vertex[v], j_vertex, visited)

            if j_vertex[v] == -1 or is_N:

                j_vertex[v] = i

                return True, j_vertex, visited

        else: 

            continue

    return False, j_vertex, visited
