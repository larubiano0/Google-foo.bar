from fractions import Fraction as frac

def solution(pegs):

    n = len(pegs) #The number of pegs is always 2 or higher
    sgn = frac(1) if n%2 == 0 else frac(-1)

    if n == 2:

        R0 = frac(2*(pegs[1]-pegs[0]),3) #After solving linear system: pegs[1] = pegs[0] + R0 + R1, R0 = 2*R1

        if R0 >= 2: #If R0 is less than 2, then R1 can't be greater than 1

            return [R0.numerator,R0.denominator]

    else: #Generalization of the linear system, adding a new equation for each extra peg

        R0 = frac(2 * sump(pegs,sgn,n),frac(2)+sgn)

        if R0 < 2: 

            return [-1,-1]
        
        k = pegs[0] 

        Ri = R0 #Radius of the i-th peg

        i = 1 #The index of the current peg

        while k<pegs[-1]: #Verify all the radius are greater or equal to 1, until k = pegs[-1] 

            k += Ri
            Ri = pegs[i] - k #Radius of the current peg

            if Ri < 1:

                return [-1,-1]

            k += Ri #Move to the center of the current peg

            i += 1 #Move to the next peg

        return [R0.numerator,R0.denominator]

    return [-1,-1] #If the above conditions are not met, then the solution is not possible


def sump(pegs,sgn,n): #Computes an alternating series

    s = frac(0) #The sum of the alternating series
    s2 = frac(0) #Part of the series that is later multiplied by 2
    s += frac(- pegs[0] + sgn * pegs[-1])

    for i in xrange(1,n-1): #Iterate from n = 1 to n-2 inclusive

        if i % 2 == 1: #Raising (-1)**(i+1) is ineficient

            s2 += frac(pegs[i]) 

        else:

            s2 -= frac(pegs[i])

    s += 2 * s2

    return s