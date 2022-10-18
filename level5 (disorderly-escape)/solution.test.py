import solution

def main():
    try: 

        assert solution.solution('77') == '4208'
        assert solution.solution('5') == '19'
        assert solution.solution('56836') == '2284200653'
        assert solution.solution('162863') == '18755586268'
        assert solution.solution('171368') == '20765634270'

        print("All tests passed")

    except AssertionError:

        print("FAILED")
        exit(1)

if __name__ == "__main__":
    main()
