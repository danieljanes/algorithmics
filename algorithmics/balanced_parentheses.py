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


from typing import Any, List, Tuple

from algorithmics.stack import Stack


def balanced_parentheses(s: str, a: List[Tuple[str, str]]) -> bool:
    opening_chars = [x[0] for x in a]
    closing_chars = [x[1] for x in a]

    stack = Stack()

    for c in s:
        if c in opening_chars:
            stack.push(c)
        else:
            if stack.is_empty():
                return False
            c_popped = stack.pop()
            for p_open, p_close in a:
                if p_open == c_popped:
                    if p_close is not c:
                        return False
    return stack.is_empty()
