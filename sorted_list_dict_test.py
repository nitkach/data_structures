from sorted_list_dict import SortedListDict


def create_sorted_dict():
    return SortedListDict.from_array([('aaa', 10), ('bbb', 20), ('ccc', 30)])


def test_smoke_set():
    d = SortedListDict()

    assert str(d) == "[]"

    d.set('aaa', 10)
    assert str(d) == "[('aaa', 10)]"

    d.set('bbb', 20)
    assert str(d) == "[('aaa', 10), ('bbb', 20)]"

    d.set('ccc', 30)
    assert str(d) == "[('aaa', 10), ('bbb', 20), ('ccc', 30)]"


def test_set_into_empty():
    d = SortedListDict()

    assert d.set('aaa', 10) is None

    assert str(d) == "[('aaa', 10)]"


def test_set_key_with_lower_value():
    d = SortedListDict()

    assert d.set('ccc', 30) is None
    assert str(d) == "[('ccc', 30)]"

    assert d.set('bbb', 20) is None
    assert str(d) == "[('bbb', 20), ('ccc', 30)]"

    assert d.set('aaa', 10) is None
    assert str(d) == "[('aaa', 10), ('bbb', 20), ('ccc', 30)]"


def test_set_key_with_greater_value():
    d = SortedListDict()

    assert d.set('aaa', 10) is None
    assert str(d) == "[('aaa', 10)]"

    assert d.set('bbb', 20) is None
    assert str(d) == "[('aaa', 10), ('bbb', 20)]"

    assert d.set('ccc', 30) is None
    assert str(d) == "[('aaa', 10), ('bbb', 20), ('ccc', 30)]"


def test_set_key_already_exist_one_element():
    d = SortedListDict()

    assert d.set('aaa', 10) is None

    assert d.set('aaa', 20) == 10

    assert str(d) == "[('aaa', 20)]"


def test_set_key_already_exist_many_elements():
    d = SortedListDict()

    assert d.set('aaa', 10) is None

    assert d.set('bbb', 20) is None

    assert d.set('ccc', 30) is None

    assert d.set('bbb', 100) == 20

    assert str(d) == "[('aaa', 10), ('bbb', 100), ('ccc', 30)]"


def test_smoke_get():
    d = create_sorted_dict()

    assert d.get('aaa') == 10


def test_get_from_empty():
    d = SortedListDict()

    assert d.get('aaa') is None


def test_get_non_existent_key():
    d = create_sorted_dict()

    assert d.get('ddd') is None


def test_remove_from_empty():
    d = SortedListDict()

    assert d.remove('aaa') is None


def test_remove_with_single_element():
    d = SortedListDict()

    assert d.set('aaa', 10) is None
    assert str(d) == "[('aaa', 10)]"

    assert d.remove('aaa') == 10
    assert str(d) == "[]"


def test_remove_head_among_several_element():
    d = create_sorted_dict()

    assert d.remove('aaa') == 10
    assert str(d) == "[('bbb', 20), ('ccc', 30)]"


def test_remove_middle_among_several_elements():
    d = create_sorted_dict()

    assert d.remove('bbb') == 20
    assert str(d) == "[('aaa', 10), ('ccc', 30)]"


def test_remove_tail_among_several_elements():
    d = create_sorted_dict()

    assert d.remove('ccc') == 30
    assert str(d) == "[('aaa', 10), ('bbb', 20)]"


def test_remove_non_existing_head_element_among_one_element():
    d = SortedListDict()

    d.set('bbb', 20)

    assert d.remove('aaa') is None


def test_remove_non_existing_tail_element_among_one_element():
    d = SortedListDict()

    d.set('bbb', 20)

    assert d.remove('ccc') is None


def test_remove_non_existing_head_element_among_several_elements():
    d = create_sorted_dict()

    assert d.remove('aa') is None


def test_remove_non_existing_middle_element_among_several_elements():
    d = create_sorted_dict()

    assert d.remove('bbc') is None


def test_remove_non_existing_tail_element_among_several_elements():
    d = create_sorted_dict()

    assert d.remove('ddd') is None
