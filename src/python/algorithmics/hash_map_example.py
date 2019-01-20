from algorithmics.hash_map import HashMap
from algorithmics.hash_map import SimpleHashMap


pairs = [('k0', 'v0'), ('k1', 10), (20, 'v2'), (30, 30)]


def main():
    # SimpleHashMap
    shm = SimpleHashMap()
    print("\nInitial SimpleHashMap:")
    print(shm)
    print("\nInsert", pairs)
    shm.insert_tuples(pairs)
    print(shm)
    # HashMap
    print("\nInitial HashMap:")
    hm = HashMap()
    print(hm)
    print("\nInsert", pairs)
    hm.insert_tuples(pairs)
    print(hm)


if __name__ == "__main__":
    main()
