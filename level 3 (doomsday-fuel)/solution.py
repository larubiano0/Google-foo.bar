from fractions import Fraction as frac


def solution(m):

    for i in xrange(len(m)): # for each row of the matrix

        m[i] = scale(m[i], i) # scale each row, to make it a prob. space and have a proper transition matrix (right stochastic matrix for a discrete markov chain)

    '''
    Here I used the book Adventures in Stochastic Processes (1992),
    by Sidney Resnick. p 102-116 (Markov Chains: Absorption probabilities)
    to help me solve this problem.
    ''' 

    
    

def scale(v,i): # scale to make the sum of its components = 1, useful for making each row of the matrix a proper transition matrix
    s = frac(sum(v))

    if s==0: 

        return [frac(0) if j != i else frac(1) for j in xrange(len(v))] # if the row is the 0 vector, the probability of going to itself is 1, otherwise it is 0

    nv = [frac(j / s) for j in v]

    return nv
