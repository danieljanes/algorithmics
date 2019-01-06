from algorithmics.search import binary_search
from algorithmics.search import linear_search


def main():
    # Linear Search
    l = [1, 56, 50, 2, 44, 25, 17, 4]  # distinct integers
    k = 17
    r = linear_search(l, k)
    print("Searching for", k, "in list", l, "using linear search returned", r)
    # Binary Search
    l = [1, 2, 4, 17, 25, 44, 50, 56]  # sorted list
    k = 16
    r = binary_search(l, k)
    print("Searching for", k, "in list", l, "using binary search returned", r)
    k = 17
    r = binary_search(l, k)
    print("Searching for", k, "in list", l, "using binary search returned", r)


if __name__ == "__main__":
    main()
