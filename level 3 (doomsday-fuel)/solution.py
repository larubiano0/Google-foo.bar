from fractions import Fraction as frac
from numpy import linalg as LA



def solution(m):

    for i in xrange(len(m)): # for each row of the matrix

        m[i] = scale(m[i]) # scale each row, to make it a prob. space and have a proper transition matrix (right stochastic matrix).

        w, v = LA.eig(m) # get the eigenvalues and eigenvectors of the matrix.

        print(v)

        print(w)
    
    

def scale(v): # scale to make the sum of its components = 1, useful for making each row of the matrix 
    s = frac(sum(v))

    if s==0: 

        return [frac(0) for _ in v] # if the vector is the 0 vector, return the 0 vector. (terminal state)

    nv = [frac(j / s) for j in v]

    return nv
