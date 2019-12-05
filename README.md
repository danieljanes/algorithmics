# Algorithmics

## Introduction

Educational implementations of common algorithms and data structures.

    Warning: The provided implementations are for educational purposes only. The implementations are not production grade and the testing is neither complete nor comprehensive.

Data structures:

- `HashMap`: A reimplementation of CPython's built-in `dict` using optimized probing
- `SimpleHashMap`: A simplified reimplementation of CPython's built-in `dict` using linear probing
- `Stack`: LIFO linear data structure implemented using a linked list
- `Queue`: FIFO linear data structure implemented using a linked list
- `StackBasedQueue`: FIFO linear data structure implemented using two stacks

Algorithms:

- Binary Search: O(log n) search on sorted lists
- Linear Search: O(n) search on unsorted lists

## Prerequisites

This project requires [Python 3](https://python.org) and uses [Bazel](https://bazel.build).

```shell
git clone git@github.com:danieljanes/algorithmics.git
cd algorithmics
bazel run //algorithmics:hash_map_example
```

## Run Example

```shell
bazel run //algorithmics:stack_example
```

## Test

```shell
bazel test //algorithmics:all
```

For more detailed test outputs pass the `--test_verbose_timeout_warnings` flag:

```shell
bazel  test //algorithmics:all --test_verbose_timeout_warnings
```
