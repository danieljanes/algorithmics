from algorithmics.stack import Stack


def test_empty():
    s = Stack()
    try:
        s.peek()
        fail()
    except:
        pass
    try:
        s.pop()
        fail()
    except:
        pass
    assert len(s) == 0


def test_single_push_peek_pop():
    s = Stack()
    s.push(0)
    assert len(s) == 1
    v = s.peek()
    assert v == 0
    v = s.pop()
    assert v == 0
    assert len(s) == 0


def test_multiple():
    s = Stack()
    vs = "Hello, world!"
    for v in vs:
        s.push(v)
        assert v == s.peek()
    xs = ""
    while len(s) > 0:
        xs = s.pop() + xs
    assert xs == vs
