def solution(s):

    salutes = 0 #Total number of salutes

    gsigns = 0 #> sings counter

    for i in s: #Iterate over the string from left to right.

        if i == '>': 
            
            gsigns += 1 #Increment > sings counter

        if i == '<':
            
            salutes += gsigns * 2 #If a < is found, add the number of > sings to the left * 2 to the total number of salutes.

    return salutes