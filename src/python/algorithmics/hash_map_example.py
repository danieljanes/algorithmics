from algorithmics.hash_map import SimpleHashMap


pairs = [('k0', 'v0'), ('k1', 1), (2, 'v2'), (3, 3)]


def main():
    hm = SimpleHashMap()
    hm.insert_tuples(kv_pairs)
    print(hm)


if __name__ == "__main__":
    main()
