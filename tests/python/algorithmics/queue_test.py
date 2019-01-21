from algorithmics.queue import Queue
from algorithmics.queue import StackBasedQueue


def test_Queue_empty():
    q = Queue()
    try:
        s.peek()
        fail()
    except:
        pass
    try:
        s.dequeue()
        fail()
    except:
        pass
    assert q.is_empty()
    assert len(q) == 0


def test_Queue_single_enqueue_peek_dequeue():
    q = Queue()
    q.enqueue(0)
    assert not q.is_empty()
    assert len(q) == 1
    v = q.peek()
    assert v == 0
    v = q.dequeue()
    assert v == 0
    assert q.is_empty()
    assert len(q) == 0


def test_Queue_multiple():
    q = Queue()
    vs = "Hello, world!"
    for v in vs:
        q.enqueue(v)
        assert vs[0] == q.peek()
    xs = ""
    while not q.is_empty():
        xs += q.dequeue()
    assert xs == vs


def test_StackBasedQueue_empty():
    q = StackBasedQueue()
    try:
        s.peek()
        fail()
    except:
        pass
    try:
        s.dequeue()
        fail()
    except:
        pass
    assert q.is_empty()
    assert len(q) == 0


def test_StackBasedQueue_single_enqueue_peek_dequeue():
    q = StackBasedQueue()
    q.enqueue(0)
    assert not q.is_empty()
    assert len(q) == 1
    v = q.peek()
    assert v == 0
    v = q.dequeue()
    assert v == 0
    assert q.is_empty()
    assert len(q) == 0


def test_StackBasedQueue_multiple():
    q = StackBasedQueue()
    vs = "Hello, world!"
    for v in vs:
        q.enqueue(v)
        assert vs[0] == q.peek()
    xs = ""
    while not q.is_empty():
        xs += q.dequeue()
    assert xs == vs
