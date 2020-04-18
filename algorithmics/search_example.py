# Copyright 2020 Daniel J. Beutel. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


from algorithmics.search import binary_search, linear_search


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
