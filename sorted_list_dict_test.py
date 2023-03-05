from sorted_list_dict import SortedListDict


def create_sorted_dict():
    return SortedListDict.from_array([('asd', 10), ('bfe', 100), ('cmd', 70)])


def test_smoke_set():
    d = SortedListDict()

    assert str(d) == "[]"

    d.set('asd', 13)
    assert str(d) == "[('asd', 13)]"

    d.set('ase', 43)
    assert str(d) == "[('asd', 13), ('ase', 43)]"

    d.set('trf', 34)
    assert str(d) == "[('asd', 13), ('ase', 43), ('trf', 34)]"


def test_set_key_already_exist_one_element():
    d = SortedListDict()

    assert d.set('asd', 10) is None

    assert d.set('asd', 20) == 10

    assert str(d) == "[('asd', 20)]"


def test_set_key_already_exist_many_elements():
    d = SortedListDict()

    assert d.set('asd', 10) is None

    assert d.set('bfe', 20) is None

    assert d.set('cmd', 70) is None

    assert d.set('bfe', 100) == 20

    assert str(d) == "[('asd', 10), ('bfe', 100), ('cmd', 70)]"


def test_smoke_get():
    d = create_sorted_dict()

    assert d.get('asd') == 10


def test_get_non_existent_key():
    d = create_sorted_dict()

    assert d.get('gfv') is None


def test_get_from_empty_dict():
    d = SortedListDict()

    assert d.get('gft') is None
