from list import List


def create_list():
    return List.from_array(['p', 'o', 'n', 'y'])


def test_push_into_empty():
    list = List()

    list.push('X')

    assert str(list) == "[X]"


def test_push_into_non_empty():
    list = create_list()

    list.push('X')

    assert str(list) == "[p, o, n, y, X]"


def test_insert_into_empty_success():
    list = List()

    list.insert(0, 'X')

    assert list == List.from_array(['X'])


def test_insert_into_empty_fail():
    list = List()

    actual_exception = None

    try:
        list.insert(1, 'X')
    except Exception as exception:
        actual_exception = exception

    assert "Index 1 is out of bound" in str(actual_exception)


def test_insert_head_into_non_empty_success():
    list = create_list()
    list.insert(0, 'X')
    assert list == List.from_array(['X', 'p', 'o', 'n', 'y'])


def test_insert_middle_into_non_empty_success():
    list = create_list()
    list.insert(1, 'X')
    assert list == List.from_array(['p', 'X', 'o', 'n', 'y'])

    list = create_list()
    list.insert(2, 'X')
    assert list == List.from_array(['p', 'o', 'X', 'n', 'y'])


def test_insert_tail_into_non_empty_success():
    list = create_list()
    list.insert(3, 'X')
    assert list == List.from_array(['p', 'o', 'n', 'X', 'y'])


def test_insert_len_into_non_empty_success():
    list = create_list()
    list.insert(4, 'X')
    assert list == List.from_array(['p', 'o', 'n', 'y', 'X'])


def test_insert_into_non_empty_fail():
    list = create_list()

    actual_exception = None

    try:
        list.insert(5, 'X')
    except Exception as exception:
        actual_exception = exception

    assert "Index 5 is out of bound" in str(actual_exception)


def test_remove_from_empty_fail():
    list = List()

    actual_exception = None

    try:
        list.remove(0)
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_remove_head_from_non_empty_success():
    list = create_list()

    char = list.remove(0)

    assert char == 'p' and list == List.from_array(['o', 'n', 'y'])


def test_remove_middle_from_non_empty_success():
    list = create_list()
    char = list.remove(1)
    assert char == 'o' and list == List.from_array(['p', 'n', 'y'])

    list = create_list()
    char = list.remove(2)
    assert char == 'n' and list == List.from_array(['p', 'o', 'y'])


def test_remove_tail_from_non_empty_success():
    list = create_list()

    char = list.remove(3)

    assert char == 'y' and list == List.from_array(['p', 'o', 'n'])


def test_remove_from_non_empty_fail():
    list = create_list()

    actual_exception = None

    try:
        list.remove(4)
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_get_elem_from_empty_fail():
    list = List()

    actual_exception = None

    try:
        list[0]
    except Exception as exception:
        actual_exception = exception

    assert "Index 0 is out of bound" in str(actual_exception)


def test_get_head_elem_from_non_empty_success():
    list = create_list()

    assert list[0] == 'p'


def test_get_middle_elem_from_non_empty_success():
    list = create_list()

    assert list[1] == 'o'
    assert list[2] == 'n'


def test_get_tail_elem_from_non_empty_success():
    list = create_list()

    assert list[3] == 'y'


def test_get_elem_from_non_empty_fail():
    list = create_list()

    actual_exception = None

    try:
        list[4]
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_set_head_elem_into_non_empty_success():
    list = create_list()
    list[0] = 'X'
    assert list == List.from_array(['X', 'o', 'n', 'y'])


def test_set_middle_elem_into_non_empty_success():
    list = create_list()
    list[1] = 'X'
    assert list == List.from_array(['p', 'X', 'n', 'y'])

    list = create_list()
    list[2] = 'X'
    assert list == List.from_array(['p', 'o', 'X', 'y'])


def test_set_elem_tail_into_non_empty_success():
    list = create_list()
    list[3] = 'X'
    assert list == List.from_array(['p', 'o', 'n', 'X'])


def test_set_elem_into_non_empty_fail():
    list = create_list()

    actual_exception = None

    try:
        list[4] = 'X'
    except Exception as exception:
        actual_exception = exception

    assert "Index 4 is out of bound" in str(actual_exception)


def test_iter():
    list = create_list()

    ans = List()

    for elem in list:
        ans.push(elem)

    assert ans == list


def test_len_empty():
    list = List()

    assert len(list) == 0


def test_len_non_empty():
    list = create_list()

    assert len(list) == 4


def test_compare_equal():
    list = create_list()

    assert list == List.from_array(['p', 'o', 'n', 'y'])


def test_compare_non_equal():
    l1 = create_list()
    l2 = List.from_array(['X'])

    ans = not l1 == l2

    assert ans


def test_string_empty():
    list = List()

    assert str(list) == '[]'


def test_string_non_empty():
    list = create_list()

    assert str(list) == '[p, o, n, y]'


def test_find_elem_in_empty():
    list = List()

    assert list.find('X') is None


def test_find_existing_elem_in_non_empty():
    list = create_list()

    assert list.find('o') == 1


def test_find_non_existing_elem_in_non_empty():
    list = create_list()

    assert list.find('X') is None


def test_repeat():
    list = List.repeat(4, None)

    assert str(list) == "[None, None, None, None]"

# strange things
# def test_raises():
#     with pytest.raises(Exception) as exc_info:
#         raise Exception('some info')
