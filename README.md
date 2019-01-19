# Algorithmics

## Introduction

Educational implementations of common algorithms and data structures.

Data structures:

- `SimpleHashMap`: A simplified reimplementation of Python's built-in `dict` using linear probing
- `Stack`: LIFO queue implemented using a linked list

Algorithms:

- Binary Search: O(log n) search on sorted lists
- Linear Search: O(n) search on unsorted lists

## Prerequisites

This project requires [Python 3](https://python.org) and uses Twitter's [Pants Build System](https://pantsbuild.org) (which automatically sets itself up):

```bash
git clone git@github.com:danieljanes/algorithmics.git
cd algorithmics
./pants bootstrap
```

## Run Example

```bash
./pants run src/python/algorithmics:stack_example
```

## Static Analysis

```bash
./pants mypy src/python/algorithmics:stack
```

## Test

```bash
./pants test tests/python/algorithmics
```
