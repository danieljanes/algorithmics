from algorithmics.queue import Queue


def main() -> None:
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


if __name__ == "__main__":
    main()
