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


from algorithmics.stack import Stack


def main() -> None:
    s = Stack()
    print(f"Initial Stack, depth: {len(s)}\n{s}")
    v = 1
    s.push(v)
    print(f"Push value {v}, stack depth: {len(s)}\n{s}")
    v = 2
    s.push(v)
    print(f"Push value {v}, stack depth: {len(s)}\n{s}")
    v = 3
    s.push(v)
    print(f"Push value {v}, stack depth: {len(s)}\n{s}")
    v = s.peek()
    print(f"Peek value: {v}, stack depth: {len(s)}\n{s}")
    v = s.pop()
    print(f"Popped value {v}, stack depth: {len(s)}\n{s}")
    v = 4
    s.push(v)
    print(f"Push value {v}, stack depth: {len(s)}\n{s}")
    v = s.pop()
    print(f"Popped value {v}, stack depth: {len(s)}\n{s}")
    v = s.pop()
    print(f"Popped value {v}, stack depth: {len(s)}\n{s}")
    v = s.pop()
    print(f"Popped value {v}, stack depth: {len(s)}\n{s}")


if __name__ == "__main__":
    main()
