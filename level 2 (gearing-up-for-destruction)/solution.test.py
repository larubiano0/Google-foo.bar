import solution

if __name__ == "__main__":

    try: 

        assert solution.solution([4, 30, 50]) == [12,1]
        assert solution.solution([4, 17, 50]) == [-1,-1]

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    