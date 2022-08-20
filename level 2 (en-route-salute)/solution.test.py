import solution

if __name__ == "__main__":

    try: 

        assert solution.solution(">----<") == 2
        assert solution.solution("<<>><") == 4
        assert solution.solution("--->-><-><-->-") == 10

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    