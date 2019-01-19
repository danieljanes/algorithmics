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
