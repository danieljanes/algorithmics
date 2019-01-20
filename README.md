# Algorithmics

## Introduction

Educational implementations of common algorithms and data structures.

Data structures:

- `HashMap`: A reimplementation of CPython's built-in `dict` using optimized probing
- `SimpleHashMap`: A simplified reimplementation of CPython's built-in `dict` using linear probing
- `Stack`: LIFO queue implemented using a linked list

Algorithms:

- Binary Search: O(log n) search on sorted lists
- Linear Search: O(n) search on unsorted lists

## Prerequisites

This project requires [Python 3](https://python.org) and uses Twitter's [Pants Build System](https://pantsbuild.org) (which automatically sets itself up):

```bash
git clone git@github.com:danieljanes/algorithmics.git
cd algorithmics
./pants3 bootstrap
```

## Run Example

```bash
./pants3 run src/python/algorithmics:stack_example
```

## Static Analysis

```bash
./pants3 mypy src/python/algorithmics:stack
```

## Test

```bash
./pants3 test tests/python/algorithmics
```
