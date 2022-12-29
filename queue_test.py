from queue_1 import Queue


def create_queue():
    q1 = Queue()

    q1.put('p')
    q1.put('o')
    q1.put('n')
    q1.put('y')

    return q1


def test_len():
    q = create_queue()

    assert len(q) == 4
    assert q.length() == 4


def test_getitem():
    q1 = create_queue()
    q2 = create_queue()

    assert q1[0] == q2[0]
    assert q1[0] == q2[-len(q2)]
    assert q1[len(q1) - 1] == q2[-1]


def test_setitem():
    q1 = create_queue()
    q2 = create_queue()

    q1[0] = 'P'
    q2[0] = 'P'

    assert q1 == q2


def test_string():
    q = create_queue()

    assert str(q) == '[p, o, n, y]'


def test_equals_success():
    assert create_queue() == create_queue()


def test_equals_fail():
    q2 = create_queue()
    q2.pop()

    assert create_queue() != q2


