def solution(area): 
    array = []
    while area > 0:
        v = squareLowerThan(area)
        array.append(v)
        area -= v #Substract the biggest square smaller or equal to area. Repeat until there's no area left.
    return array

def squareLowerThan(n): #Computes the biggest square smaller or equal to n
    x = n            #Newthon's method to compute the intenger square root of n. 
    y = (x + 1) // 2 #More info: https://math.stackexchange.com/questions/34235/algorithm-for-computing-square-root-of-a-perfect-square-integer
    while y < x:
        x = y
        y = (x + n // x) // 2 #The derivative of x*x = 2x. 
    return x*x #Squaring the result to get the biggest square smaller or equal to n