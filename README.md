# Algorithmics

## Introduction

Educational implementations of a few common algorithms and data structures:

- SimpleHashMap: A simplified reimplementation of Python's built-in `dict` which uses linear probing
- Linear Search: O(n) search on unsorted lists
- Binary Search: O(log n) search on sorted lists

## Setup

### Prerequisites

Pants Build System: `https://pantsbuild.org`

```bash
git clone ...
cd algorithmics
./pants bootstrap
```

### Build Library

```bash
./pants build src/python/algorithmics:search
```

### Run Example

```bash
./pants run src/python/algorithmics:search_example
```

### Static Analysis

```bash
./pants mypy src/python/algorithmics:search
```

### Test

```bash
./pants test tests/python/algorithmics
```
