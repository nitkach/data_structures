from queue_1 import Queue


def create_queue():
    return Queue.from_array(['p', 'o', 'n', 'y'])


def test_pop_empty():
    q = Queue()

    actual_exception = None

    try:
        q.pop()
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_pop_non_empty():
    q = create_queue()

    char = q.pop()

    assert char == 'p' and str(q) == str(Queue.from_array(['o', 'n', 'y']))


def test_push_to_empty():
    q = Queue()

    q.push('X')

    assert str(q) == str(Queue.from_array(['X']))


def test_push_to_non_empty():
    q = create_queue()

    q.push('X')

    assert str(q) == str(Queue.from_array(['p', 'o', 'n', 'y', 'X']))


def test_peek_the_empty():
    q = Queue()

    actual_exception = None

    try:
        q.peek()
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_peek_the_non_empty():
    q = create_queue()

    char = q.peek()

    assert char == 'p'


def test_iter():
    q = create_queue()

    ans = Queue()

    for elem in q:
        ans.push(elem)

    assert ans == q