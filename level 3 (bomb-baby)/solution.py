def solution(x, y):

    x, y = long(x), long(y)

    s = long(0) #Number of steps

    while (x != 1) and (y != 1):

        if x<y:

            k = y//x 

            s += k

            y -= k*x

        elif y<x:

            k = x//y

            s += k

            x -= k*y

        else: 

            return 'impossible'

        if x < 1 or y < 1:

            return 'impossible'

    if x>y:

        return str(s + x - 1)

    else: 

        return str(s + y - 1)

    