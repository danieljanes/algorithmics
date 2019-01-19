# Algorithmics

## Introduction

Educational implementations of a few common algorithms and data structures.

Data structures:

- SimpleHashMap: A simplified reimplementation of Python's built-in `dict` which uses linear probing
- Stack

Algorithms:

- Binary Search: O(log n) search on sorted lists
- Linear Search: O(n) search on unsorted lists

## Setup

### Prerequisites

Pants Build System: `https://pantsbuild.org`

```bash
git clone git@github.com:danieljanes/algorithmics.git
cd algorithmics
./pants bootstrap
```

### Run Example

```bash
./pants run src/python/algorithmics:stack_example
```

### Static Analysis

```bash
./pants mypy src/python/algorithmics:stack
```

### Test

```bash
./pants test tests/python/algorithmics
```
