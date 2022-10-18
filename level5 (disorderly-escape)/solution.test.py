import solution

def main():
    try: 

        assert solution.solution(2, 3, 4) == '430'
        assert solution.solution(2, 2, 2) == '7'
        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)

if __name__ == "__main__":
    main()
