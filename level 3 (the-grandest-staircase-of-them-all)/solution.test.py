import solution

if __name__ == "__main__":

    try: 

        assert solution.solution(3) == 1
        assert solution.solution(4) == 1
        assert solution.solution(5) == 2
        assert solution.solution(8) == 5
        assert solution.solution(200) == 487067745

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)