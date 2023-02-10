from list import List


def create_list():
    return List.from_array(['p', 'o', 'n', 'y'])


def test_push_into_empty():
    l = List()

    l.push('X')

    assert l == List.from_array(['X'])


def test_push_into_non_empty():
    l = create_list()

    l.push('X')

    assert l == List.from_array(['p', 'o', 'n', 'y', 'X'])


def test_insert_into_empty_success():
    l = List()

    l.insert(0, 'X')

    assert l == List.from_array(['X'])


def test_insert_into_empty_fail():
    l = List()

    actual_exception = None

    try:
        l.insert(1, 'X')
    except Exception as exception:
        actual_exception = exception

    assert "Index 1 is out of bound" in str(actual_exception)


def test_insert_head_into_non_empty_success():
    l = create_list()
    l.insert(0, 'X')
    assert l == List.from_array(['X', 'p', 'o', 'n', 'y'])


def test_insert_middle_into_non_empty_success():
    l = create_list()
    l.insert(1, 'X')
    assert l == List.from_array(['p', 'X', 'o', 'n', 'y'])

    l = create_list()
    l.insert(2, 'X')
    assert l == List.from_array(['p', 'o', 'X', 'n', 'y'])


def test_insert_tail_into_non_empty_success():
    l = create_list()
    l.insert(3, 'X')
    assert l == List.from_array(['p', 'o', 'n', 'X', 'y'])


def test_insert_len_into_non_empty_success():
    l = create_list()
    l.insert(4, 'X')
    assert l == List.from_array(['p', 'o', 'n', 'y', 'X'])


def test_insert_into_non_empty_fail():
    l = create_list()

    actual_exception = None

    try:
        l.insert(5, 'X')
    except Exception as exception:
        actual_exception = exception

    assert "Index 5 is out of bound" in str(actual_exception)


def test_remove_from_empty_fail():
    l = List()

    actual_exception = None

    try:
        l.remove(0)
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_remove_head_from_non_empty_success():
    l = create_list()

    char = l.remove(0)

    assert char == 'p' and l == List.from_array(['o', 'n', 'y'])


def test_remove_middle_from_non_empty_success():
    l = create_list()
    char = l.remove(1)
    assert char == 'o' and l == List.from_array(['p', 'n', 'y'])

    l = create_list()
    char = l.remove(2)
    assert char == 'n' and l == List.from_array(['p', 'o', 'y'])


def test_remove_tail_from_non_empty_success():
    l = create_list()

    char = l.remove(3)

    assert char == 'y' and l == List.from_array(['p', 'o', 'n'])


def test_remove_from_non_empty_fail():
    l = create_list()

    actual_exception = None

    try:
        l.remove(4)
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_get_elem_from_empty_fail():
    l = List()

    actual_exception = None

    try:
        l[0]
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_get_head_elem_from_non_empty_success():
    l = create_list()

    assert l[0] == 'p'


def test_get_middle_elem_from_non_empty_success():
    l = create_list()

    assert l[1] == 'o'
    assert l[2] == 'n'


def test_get_tail_elem_from_non_empty_success():
    l = create_list()

    assert l[3] == 'y'


def test_get_elem_from_non_empty_fail():
    l = create_list()

    actual_exception = None

    try:
        l[4]
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_set_head_elem_into_non_empty_success():
    l = create_list()
    l[0] = 'X'
    assert l == List.from_array(['X', 'o', 'n', 'y'])


def test_set_middle_elem_into_non_empty_success():
    l = create_list()
    l[1] = 'X'
    assert l == List.from_array(['p', 'X', 'n', 'y'])

    l = create_list()
    l[2] = 'X'
    assert l == List.from_array(['p', 'o', 'X', 'y'])


def test_set_elem_tail_into_non_empty_success():
    l = create_list()
    l[3] = 'X'
    assert l == List.from_array(['p', 'o', 'n', 'X'])


def test_set_elem_into_non_empty_fail():
    l = create_list()

    actual_exception = None

    try:
        l[4] = 'X'
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_iter():
    l = create_list()

    ans = List()

    for elem in l:
        ans.push(elem)

    assert ans == l


def test_len_empty():
    l = List()

    assert len(l) == 0


def test_len_non_empty():
    l = create_list()

    assert len(l) == 4


def test_compare_equal():
    l = create_list()

    assert l == List.from_array(['p', 'o', 'n', 'y'])


def test_compare_non_equal():
    l1 = create_list()
    l2 = List.from_array(['X'])

    ans = not l1 == l2

    assert ans


def test_string_empty():
    l = List()

    assert str(l) == '[]'


def test_string_non_empty():
    l = create_list()

    assert str(l) == '[p, o, n, y]'


def test_find_elem_in_empty():
    l = List()

    assert l.find('X') == None


def test_find_existing_elem_in_non_empty():
    l = create_list()

    assert l.find('o') == 1


def test_find_non_existing_elem_in_non_empty():
    l = create_list()

    assert l.find('X') == None