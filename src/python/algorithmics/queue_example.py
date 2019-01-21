from algorithmics.queue import Queue
from algorithmics.queue import StackBasedQueue


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
