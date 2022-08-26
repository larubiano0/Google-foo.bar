import solution

if __name__ == "__main__":

    try: 

        assert solution.solution('4','7') == '4'
        assert solution.solution('2','1') == '1'
        assert solution.solution('10','3') == '5'
        assert solution.solution('2','4') == 'impossible'

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)
    