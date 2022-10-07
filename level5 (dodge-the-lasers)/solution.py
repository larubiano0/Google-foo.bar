from decimal import Decimal, getcontext

getcontext().prec = 1000


def solution(s):
    '''
    Using https://frar.ca/wordpress/?p=168 and Wikipedia https://en.wikipedia.org/wiki/Beatty_sequence
    it can be verified that the problem is equivalent to finding 
    the summation of a Partial Beatty Sequence. 
    In this case:

    Raleigh-Beatty Theorem states that a sequence,
    consisting of all the positive integers that are not
    in the sequence, is itself a Beatty sequence generated
    by a different irrational number. To find the 'complimentary' 
    Beatty sequence we should for r in the 
    equation:

    1/sqrt(2) + 1/r = 1

    Then r = 2 + sqrt(2)

    We define:

    N = floor(s*sqrt(2))

    m = floor(N/(sqrt(2)+2))

    Then using the theorem:

    \sum_{i=1}^{s} floor(i*sqrt(2)) + \sum_{j=1}^{m} floor(j*(2 + sqrt(2))) = (N^2 + N)/2

    Rearranging the terms:

    \sum_{i=1}^{s} floor(i*sqrt(2)) = (N^2 + N)/2 - \sum_{j=1}^{m} floor(j*(2 + sqrt(2)))

    and finally:

    \sum_{i=1}^{s} floor(i*sqrt(2)) = (N^2 + N)/2 - \sum_{j=1}^{m} 2*j + floor(j*sqrt(2)))

    Which by the sum of the first m natural numbers equals:

    \sum_{i=1}^{s} floor(i*sqrt(2)) = (N^2 + N)/2 - m*(m+1) - \sum_{j=1}^{m} floor(j*sqrt(2)))
    '''
    s = Decimal(s)
    return str(sol(s))

def sol(s):
    baseCases = {0: 0,
                 1: 1,}
    if s in baseCases:
        return baseCases[s]

    N = Decimal((s*Decimal(2).sqrt())//1)
    m = Decimal(N*(Decimal(2)-Decimal(2).sqrt()))//Decimal(2)

    sumation = Decimal(N*N + N)/Decimal(2)
    sumation -= Decimal(m)*Decimal(m+1)

    sumation -= Decimal(sol(m))
    return sumation
    
'''
<encrypted>
F0YBAAEKBB0cF0xbUlIFGwQPGxdAQVUWDQUNCw5XGQRVVVhJRgscRAkEHxAGTk1OSFUKBx0HFhpG TlUQSwgcFhAMBQcNXAlGXlVFCAIGBlUaBB8QDB1GTlUQSxQcGQ0KCgsLF0BBVQcDCwMHG0NLQUhV RRoACAoXQEFVEw0GRk5VEEsWGxtDThw= </encrypted>

For your eyes only!
'''