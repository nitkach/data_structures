from hash_dict import HashDict


def stable_hash(string: str) -> int:
    acc = len(string)
    for char in string:
        acc = (acc + ord(char)) % 2**64
    return acc


HashDict.hash = stable_hash


def create_sorted_dict():
    return HashDict.from_array([('asd', 10), ('bfe', 100), ('cmd', 70)])


def test_stable_hash():
    assert HashDict.hash('gfe') == 309
    assert HashDict.hash('erg') == 321
    assert HashDict.hash('nfk') == 322
    assert HashDict.hash('qwe') == 336
    assert HashDict.hash('gef') == 309
    assert HashDict.hash('gfe') == 309
    assert HashDict.hash('hfd') == 309
    assert HashDict.hash('voq') == 345


def test_set_block_size_zero():
    h = HashDict()

    h.set('gfe', 235)

    assert str(h) == "[None, None, None, None, ('gfe', 235)]"


def test_set_block_size_one():
    h = HashDict()

    h.set('qwe', 45)
    h.set('erg', 64)

    assert str(h) == "[None, ('qwe', 45), ('erg', 64), None, None]"


def test_set_block_size_two():
    h = HashDict()

    h.set('qwe', 45)
    h.set('nfk', 43)
    h.set('erg', 64)

    assert str(h) == "[None, ('qwe', 45), ('nfk', 43), ('erg', 64), None]"


def test_set_block_wrap_around():
    h = HashDict()

    h.set('gef', 342)
    assert h.set('gfe', 235) is None

    assert str(h) == "[('gfe', 235), None, None, None, ('gef', 342)]"

    h.set('hfd', 45)

    assert str(h) == "[('gfe', 235), ('hfd', 45), None, None, ('gef', 342)]"


def test_set_on_existing_key():
    h = HashDict()

    h.set('qwe', 45)
    h.set('erg', 64)

    assert h.set('qwe', 100) == 45
    assert str(h) == "[None, ('qwe', 100), ('erg', 64), None, None]"


def test_rehash():
    h = HashDict()

    h.set('qwe', 45)
    h.set('nfk', 43)
    h.set('erg', 64)
    h.set('efj', 23)
    h.set('voq', 43)
