from list import List


def create_list():
    l = List()

    l.push('p')
    l.push('o')
    l.push('n')
    l.push('y')

    return l


def test_getitem_success():
    assert create_list()[0] == 'p'

def test_getitem_fail():
    assert create_list()[0] != 'a'


def test_setitem_success():
    l1 = create_list()
    l2 = create_list()

    l1[-1] = 'k'
    l2[-1] = 'k'

    assert l1 == l2

def test_setitem_fail():
    l1 = create_list()
    l2 = create_list()

    l1[-1] = 'k'
    l2[-1] = 't'

    assert l1 != l2


def test_equals_success():
    l1 = create_list()
    l2 = create_list()

    assert l1 == l2

def test_equals_fail_element():
    l2 = create_list()
    l2[0] = 'd'
    assert create_list() != l2

def test_equals_fail_len():
    l1 = create_list()
    l1.remove(0)
    assert l1 != create_list()


def test_push_success():
    l1 = create_list()

    l1.push('t')

    assert len(l1) == len(create_list()) + 1 and l1[-1] == 't'

def test_push_fail():
    l1 = create_list()

    l1.push('t')

    assert len(l1) - 1 == len(create_list())


def test_insert_success():
    l1 = create_list()

    l1.insert(3, 'u')

    assert str(l1) == '[p, o, n, u, y]'

def test_insert_fail():
    l1 = create_list()

    l1.insert(3, 'u')

    assert str(l1) != '[p, o, n, y]'


def test_remove_success():
    l1 = create_list()
    l1.remove(0)

    l2 = create_list()
    l2.remove(0)

    assert l1 == l2

def test_remove_fail():
    l1 = create_list()
    l1.remove(0)

    assert l1 != create_list()


def test_find_success():
    l1 = create_list()

    assert l1.find('p') == 0

def test_find_fail():
    l1 = create_list()

    assert l1.find('p') != 1