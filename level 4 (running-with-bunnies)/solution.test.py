import solution

if __name__ == "__main__":

    try: 
        A = [
            [0, 2, 2, 2, -1],
            [9, 0, 2, 2, -1],
            [9, 3, 0, 2, -1],
            [9, 3, 2, 0, -1],
            [9, 3, 2, 2, 0]
            ]

        B = [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
            ]

        assert solution.solution(A,1) == [1, 2]
        assert solution.solution(B,3) == [0, 1]

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)