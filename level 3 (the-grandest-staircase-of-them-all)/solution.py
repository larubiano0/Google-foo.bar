from math import floor, sqrt

def solution(n):
    
    if n == 3:

        return 1

    elif n == 4:

        return 1

    elif n == 5:

        return 2

    hashmap = {0:1,1:1} #Initialize the hashmap with the base cases.

    hashmap.update(hashmap) #Update the hashmap with the solutions for the first 2 steps

    s, hashmap = partitionFunctionQ(n,hashmap)

    return s-1 #Removes case with only one step.


def partitionFunctionQ(n,hashmap): # generalized solution of the problem without a minimum need of 2 steps.

    '''
    Its the same as the number of sets that sum to n. k indicatetes the minimum number allowed in the set
    This closed form solution is found in https://mathworld.wolfram.com/PartitionFunctionQ.html
    '''

    if n in hashmap:

        return hashmap[n], hashmap

    n_j = nj() #Finds all n:j pairs for n<=200 

    if n in n_j:

        j = n_j[n]

        sn = 1 if (j % 2 == 0) else -1

    else: 

        sn = 0

    s = 0 # initialise sum to be returned.

    for i in range(1, int(floor(sqrt(n)) + 1)): #Alternating series with memoization.

        pm = -1 if (i % 2 == 0) else 1 # +1 for even, -1 for odd.

        Qnk2, hashmap = partitionFunctionQ(n - i*i, hashmap) #Recursive call to the function.

        s += pm * Qnk2 #Add the result to the sum.

    s = sn + 2 * s

    hashmap[n] = s #Update the hashmap.

    return s, hashmap

def nj():
    '''
    Finds all n:j pairs for n<=200 such that n=j*(3j+1)/2 or n=j*(3*j-1)/2
    '''

    sn = {} #Hashmap with all n:j pairs for n<=200

    j = 1

    while True:

        #n1 and n2 its always a natural number. For odd cases a = (3*j(+-)1) is even,
        #  then a/2 is in N, then a is even. For even cases j is even, then j*a/2 is in N.

        n1 = (j*(3*j+1))/2
        n2 = (j*(3*j-1))/2

        sn[n1] = j
        sn[n2] = j

        j += 1

        if n2 > 200:
            break

    return sn