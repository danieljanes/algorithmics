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


from algorithmics.queue import Queue, StackBasedQueue


def main() -> None:
    print("\nQueue (using linked list):\n")

    q = Queue()
    print(f"Initial queue, length: {len(q)}\n{q}")
    v = 1
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = 2
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = 3
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = q.peek()
    print(f"Peek value: {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = 4
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")

    print("\n\nStackBasedQueue:\n")

    q = StackBasedQueue()
    print(f"Initial queue, length: {len(q)}\n{q}")
    v = 1
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = 2
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = 3
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = q.peek()
    print(f"Peek value: {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = 4
    q.enqueue(v)
    print(f"Enqueue value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")
    v = q.dequeue()
    print(f"Dequeued value {v}, queue length: {len(q)}\n{q}")


if __name__ == "__main__":
    main()
