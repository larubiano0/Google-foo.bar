from itertools import permutations


def solution(times, times_limit):

    has_cycle, dist = FloydWarshall(times)

    if has_cycle: #If there is a negative cycle, all the bunnies can be saved.

        return [i for i in xrange(len(times) - 2)]

    else:

        string = ''.join([str(x) for x in xrange(len(times) - 2)]) #The string of bunnies to be saved.
        cases = stringCombination(string) #Generate all possible combinations of bunnies. 
        cases.append('') #Appends empty case for the case where no bunnies are saved.
        cases = sorted(cases, key=len, reverse=True) #Sort from shortest to longest string, reverses the list to ensure that the first case that is found is the case with the most bunnies saved.

        for path in cases:

            case = 'B'  + path + 'S' #Add the start and Bulkhead to the case.
            cost = calculateCost(case,dist)

            if cost <= times_limit:

                return sorted([int(x) for x in path])
    

def FloydWarshall(M):

    '''
    Takes an adjacency matrix M and returns True, dist if there is a negative cycle in M, False, dist otherwise.
    Floyd-Warshall algorithm modification for Cycle Detection.
    Dist is the minimum distance from a vertex to all other vertices.
    '''    

    dist=[[0 for i in xrange(len(M))] for j in xrange(len(M))]
      
    for i in xrange(len(M)):

        for j in xrange(len(M)):

            dist[i][j] = M[i][j]
      

    for k in xrange(len(M)):
     
        for i in xrange(len(M)):
                  
            for j in xrange(len(M)):

                if (dist[i][k] + dist[k][j] < dist[i][j]):
                        dist[i][j] = dist[i][k] + dist[k][j]


    for i in xrange(len(M)):

        if (dist[i][i] < 0): # If there is a negative cycle, the distance to itself will be negative.

            return True, dist
  
    return False, dist


def stringCombination(string):

    '''
    Takes a string and returns a list of all possible combinations of the string in lexigraphical order. 
    325 cases in the worst case (The number of bunnies is 5). (https://oeis.org/A007526)
    '''

    return [''.join(p) for i in xrange(len(string)) for p in permutations(string, i+1)]


def calculateCost(string,dist):
    '''
    Takes path string of the form:
    End - Node n - Node n-1 ... - Node 1 - Start
    and returns the cost of the path.
    '''
    cost = 0

    k = len(string) - 1

    while k>0:

        cost += dist[toIndex(string[k],dist)][toIndex(string[k-1],dist)]

        k-=1
    
    return cost


def toIndex(i, dist):

    if i == 'S':

        return 0

    elif i == 'B': 

        return len(dist) - 1

    else: 

        return int(i) + 1
