import solution

if __name__ == "__main__":

    try: 

        assert solution.solution(15324) == [15129,169,25,1]
        assert solution.solution(1) == [1]
        assert solution.solution(12) == [9,1,1,1]

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    

