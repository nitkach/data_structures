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


def test_equals_success():
    q1 = create_queue()
    q2 = create_queue()

    assert q1 == q2

def test_equals_fail_element():
    q1 = create_queue()
    q1[0] = 'd'

    assert q1 != create_queue()

def test_equals_fail_len():
    q1 = create_queue()
    q1.pop()

    assert q1 != create_queue()


def test_getitem_success():
    q1 = create_queue()

    assert q1[0] == q1[-len(q1)]

def test_getitem_fail():
    q1 = create_queue()

    assert q1[0] != q1[1]


def test_setitem_success():
    q1 = create_queue()

    q1[0] = 'P'

    assert q1[0] == 'P'

def test_setitem_fail():
    q1 = create_queue()

    q1[0] = 'P'

    assert q1 != create_queue()


def test_string():
    q1 = create_queue()

    assert str(q1) == '[p, o, n, y]'


def test_find_success():
    q1 = create_queue()

    assert q1.find('p') == 0


def test_find_fail():
    q1 = create_queue()
    
    assert q1.find('x') == None