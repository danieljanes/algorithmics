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


from typing import Any, List


def linear_search(list: List[Any], key: Any) -> bool:
    i: int = 0
    while i < len(list):
        if list[i] == key:
            return True
        i += 1
    return False


def binary_search(list: List[Any], key: Any) -> bool:
    l: int = 0
    r: int = len(list) - 1
    while l < r:
        i: int = l + (r - l) // 2
        item = list[i]
        if item == key:
            return True
        elif item > key:
            r = i - 1
        else:
            l = i + 1
    return False
