from queue_1 import Queue


def create_queue():
    return Queue.from_array(['p', 'o', 'n', 'y'])


def test_pop_in_empty_fail():
    q = Queue()

    actual_exception = None

    try:
        q.pop()
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_pop_in_non_empty_success():
    q = create_queue()

    char = q.pop()

    assert char == 'p' and q == Queue.from_array(['o', 'n', 'y'])


def test_push_to_empty():
    q = Queue()

    q.push('X')

    assert q == Queue.from_array(['X'])


def test_push_to_non_empty():
    q = create_queue()

    q.push('X')

    assert q == Queue.from_array(['p', 'o', 'n', 'y', 'X'])


def test_peek_the_empty_fail():
    q = Queue()

    actual_exception = None

    try:
        q.peek()
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_peek_the_non_empty_success():
    q = create_queue()

    char = q.peek()

    assert char == 'p'


def test_iter():
    q = create_queue()

    ans = Queue()

    for elem in q:
        ans.push(elem)

    assert ans == q


def test_len_empty():
    q = Queue()

    assert len(q) == 0


def test_len_non_empty():
    q = create_queue()

    assert len(q) == 4


def test_compare_equal():
    q = create_queue()

    assert q == Queue.from_array(['p', 'o', 'n', 'y'])


def test_compare_non_equal():
    q1 = create_queue()
    q2 = Queue.from_array(['X'])

    ans = not q1 == q2

    assert ans


def test_string_empty():
    q = Queue()

    assert str(q) == '[]'


def test_string_non_empty():
    q = create_queue()

    assert str(q) == '[p, o, n, y]'


def test_find_elem_in_empty():
    q = Queue()

    assert q.find('X') == None


def test_find_elem_in_non_empty():
    q = create_queue()

    assert q.find('o') == 1


def test_find_elem_in_non_empty_fail():
    q = create_queue()

    assert q.find('X') == None