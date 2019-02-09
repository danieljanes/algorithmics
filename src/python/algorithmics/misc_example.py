from algorithmics.misc import find_missing_int_using_hash_map
from algorithmics.misc import find_missing_int_using_sum


def main():
    complete = [4, 8, 12, 9, 3]
    incomplete = [4, 8, 9, 3]
    
    print("Complete:  ", complete)
    print("Incomplete:", incomplete)

    print("\n\tMissing int determined using hash map:", end="")
    print(find_missing_int_using_hash_map(complete, incomplete))
    print("\n\tMissing int determined using summation:", end="")
    print(find_missing_int_using_sum(complete, incomplete))


if __name__ == "__main__":
    main()
