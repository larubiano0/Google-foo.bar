import solution

if __name__ == "__main__":

    try: 

        assert solution.solution([10]) == 1
        assert solution.solution([1,1]) == 2
        assert solution.solution([7, 4]) == 0
        assert solution.solution([1, 10, 7, 3, 21, 13, 109, 21, 13, 19, 1, 7, 3, 21, 13, 19, 3, 54]) == 0
        assert solution.solution([1, 7, 3, 21, 13, 109, 21, 13, 19, 1, 7, 3, 21, 13, 19, 3, 54]) == 1
        assert solution.solution([1, 7, 3, 21, 13, 19]) == 0

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    