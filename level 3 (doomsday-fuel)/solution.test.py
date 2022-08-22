import solution

if __name__ == "__main__":

    try: 

        M = [
            [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
            [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
            [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
            [0,0,0,0,0,0],  # s3 is terminal
            [0,0,0,0,0,0],  # s4 is terminal
            [0,0,0,0,0,0],  # s5 is terminal
            ]

        assert solution.solution(M) == [0, 3, 2, 9, 14]

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    