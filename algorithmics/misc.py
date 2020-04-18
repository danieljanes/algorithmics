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


from algorithmics.hash_map import HashMap


def find_missing_int_using_hash_map(complete, incomplete):
    """
    Problem: There are distinct integers in list `complete`. The same integers are in list `incomplete`, except for one.
    
    Task: Find the one integer which is missing from the incomplete list.

    Algorithm:
    - Insert all elements of the shorter list into a hash map
    - Then test each element of the full list for presence

    Complexity: O(n) time, O(n) space
    """
    hm = HashMap()  # Or use dict()
    for i in incomplete:
        hm[i] = 1
    for j in complete:
        if j not in hm:
            return j


def find_missing_int_using_sum(complete, incomplete):
    """
    Problem: There are distinct integers in list `complete`. The same integers are in list `incomplete`, except for one.
    
    Task: Find the one integer which is missing from the incomplete list.

    Complexity: O(n) time, O(1) space
    """
    s = 0
    for a, b in zip(complete[:-1], incomplete):
        s += a
        s -= b
    return s + complete[len(complete) - 1]
