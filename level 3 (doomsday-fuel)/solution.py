from fractions import Fraction as frac
from fractions import gcd


def solution(m):

    terminals = []

    for i in xrange(len(m)): # for each row of the matrix

        m[i], state = scale(m[i], i) # scale each row, to make it a prob. space and have a proper transition matrix (right stochastic matrix for a discrete markov chain))

        if state == 't': # if the row is a terminal state, add it to the list of terminals

            terminals.append(i)

    '''
    Here I used the book Adventures in Stochastic Processes (1992),
    by Sidney Resnick. p 102-116 (Markov Chains: Absorption probabilities)
    to help me solve this problem.
    ''' 

    # m = ([Q, R].
    #      [0, P2]) 
    
    dimQ = len(m) - len(terminals) # number of rows/columns in Q

    Q, R = [], []
    
    for i in xrange(len(m)):  # intialize Q and R, with the appropriate dimensions

        colQ = []
        colR = []

        for j in xrange(len(m)):

            if j < dimQ:

                colQ.append(m[i][j])

            else: 

                colR.append(m[i][j])

        Q.append(colQ)
        R.append(colR)

        if i == dimQ - 1:

            break

    IQ = identity(dimQ) # identity matrix of dimension Q

    S = matrixDif(IQ, Q) # S = I - Q
    T = invertMatrix(S, IQ) # T = (I - S)^-1
    U = matrixMultiply(T, R) # U = (I - S)^-1 * R

    probs =  U[0] #We only need the first row of the matrix, since we started on the first state. 

    numerators = [probs[i].numerator for i in xrange(len(probs))] # get the numerators of the probabilities
    denominators = [probs[i].denominator for i in xrange(len(probs))] # get the denominators of the probabilities

    denominator = lcm(denominators) # common denominator

    sol = [] # array to be returned

    for i in xrange(len(probs)):

        multiple = denominator / denominators[i] # scale the denominators to the common denominator

        sol.append(numerators[i]*multiple) # add the scaled numerators to the array

    sol.append(denominator) # add the common denominator to the array

    return sol


def scale(v,i): # scale to make the sum of its components = 1, useful for making each row of the matrix a proper transition matrix

    s = frac(sum(v))

    if s==0: 

        return [frac(0) if j != i else frac(1) for j in xrange(len(v))], 't' # if the row is the 0 vector, the probability of going to itself is 1, otherwise it is 0
                                                                             # t for terminal state
    nv = [frac(j / s) for j in v]

    return nv, 'nt' #not terminal state


def identity(dim): # returns the identity matrix of dimension dim^2. eg: identity(2) = [[1,0],[0,1]]
    return [[frac(1) if i==j else frac(0) for i in xrange(dim)] for j in xrange(dim)]


def matrixDif(A,B): # returns the difference of two matrices of the same dimension A + (-1)B
    return [[frac(A[i][j] - B[i][j]) for j in xrange(len(A[0]))] for i in xrange(len(A))]


def invertMatrix(M, I): #Modified from https://github.com/ThomIves/MatrixInverse
    for fd in xrange(len(M)):
        fdScaler = frac(1,M[fd][fd])
        for j in xrange(len(M)):
            M[fd][j] = frac(M[fd][j] * fdScaler)
            I[fd][j] = frac(I[fd][j] * fdScaler)
        for i in list(xrange(len(M)))[0:fd] + list(xrange(len(M)))[fd+1:]:
            crScaler = M[i][fd]
            for j in xrange(len(M)):
                M[i][j] = frac(M[i][j] - frac(crScaler * M[fd][j]))
                I[i][j] = frac(I[i][j] - frac(crScaler * I[fd][j]))
    return I


def matrixMultiply(A, B):

    C = zeroMatrix(len(A), len(B[0]))

    for i in range(len(A)):

        for j in range(len(B[0])):

            for k in range(len(B)):

                C[i][j] = frac(C[i][j] + frac(A[i][k] * B[k][j]))

    return C


def zeroMatrix(n,m): #Initializes a matrix of dimension n x m with all zeros
    return [[frac(0) for j in xrange(m)] for i in xrange(n)]


def lcm(array): #lcm of an array

    lcm = 1

    for i in array:

        lcm = lcm*i//gcd(lcm, i)

    return lcm