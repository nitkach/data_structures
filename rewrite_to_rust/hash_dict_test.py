from hash_dict import HashDict


def stable_hash(string: str) -> int:
    acc = len(string)
    for char in string:
        acc = (acc + ord(char)) % 2**64
    return acc


HashDict.hash = stable_hash


def create_hashmap():
    return HashDict.from_array([('aaaaa', 10)])


def test_stable_hash():
    assert HashDict.hash('aaaaa') == 490
    assert HashDict.hash('aaaab') == 491
    assert HashDict.hash('aaaac') == 492
    assert HashDict.hash('aaaad') == 493
    assert HashDict.hash('aaaae') == 494

    assert HashDict.hash('aaaaf') == 495
    assert HashDict.hash('aaaag') == 496
    assert HashDict.hash('aaaah') == 497
    assert HashDict.hash('aaaai') == 498
    assert HashDict.hash('aaaaj') == 499

    assert HashDict.hash('aaaak') == 500

    assert HashDict.hash('gef') == 309
    assert HashDict.hash('hfd') == 309
    assert HashDict.hash('erg') == 321
    assert HashDict.hash('nfk') == 322
    assert HashDict.hash('qwe') == 336
    assert HashDict.hash('toq') == 343
    assert HashDict.hash('uoq') == 344
    assert HashDict.hash('voq') == 345


def test_set_block_size_zero():
    h = HashDict()

    assert h.set('aaaaa', 10) is None

    assert str(h) == "[('aaaaa', 10), None, None, None, None]"


def test_set_block_size_one():
    h = HashDict()

    assert h.set('aaaab', 20) is None
    assert h.set('aaaac', 30) is None

    assert str(h) == "[None, ('aaaab', 20), ('aaaac', 30), None, None]"


def test_set_block_size_two():
    h = HashDict()

    assert h.set('aaaab', 20) is None
    assert h.set('aaaac', 30) is None
    assert h.set('aaaad', 40) is None

    assert str(h) == "[None, ('aaaab', 20), ('aaaac', 30), ('aaaad', 40), None]"


def test_set_block_wrap_around():
    h = HashDict()

    assert h.set('aaaae', 50) is None
    assert h.set('aaaaa', 10) is None

    assert str(h) == "[('aaaaa', 10), None, None, None, ('aaaae', 50)]"

    h.set('aaaaj', 500)

    assert str(h) == "[('aaaaa', 10), ('aaaaj', 500), None, None, ('aaaae', 50)]"


def test_set_on_existing_key():
    h = HashDict()

    h.set('aaaab', 20)
    h.set('aaaac', 30)

    assert h.set('aaaab', 200) == 20
    assert str(h) == "[None, ('aaaab', 200), ('aaaac', 30), None, None]"


def test_set_on_existing_key_and_wrap_around():
    h = HashDict()

    assert h.set('aaaae', 50) is None
    assert h.set('aaaaa', 10) is None

    assert str(h) == "[('aaaaa', 10), None, None, None, ('aaaae', 50)]"

    h.set('aaaaj', 500)

    assert str(h) == "[('aaaaa', 10), ('aaaaj', 500), None, None, ('aaaae', 50)]"

    assert h.set('aaaaj', 5000) == 500

    assert str(h) == "[('aaaaa', 10), ('aaaaj', 5000), None, None, ('aaaae', 50)]"


def test_smoke_get():
    h = HashDict()

    assert h.get('any') is None

    h.set('aaaaa', 10)

    assert h.get('aaaaa') == 10

    h.set('aaaab', 20)

    assert h.get('aaaab') == 20
    assert h.get('aaaaa') == 10
    assert h.get('any') is None


def test_get_from_not_initialized():
    h = HashDict()

    assert h.get('any') is None


def test_get_from_empty():
    h = HashDict()

    h.set('aaaae', 50)

    assert h.remove('aaaae') == 50
    assert str(h) == "[None, None, None, None, None]"


def test_get_block_size_one():
    h = create_hashmap()

    assert h.get('aaaaa') == 10
    assert str(h) == "[('aaaaa', 10), None, None, None, None]"


def test_get_block_size_two():
    h = create_hashmap()

    h.set('aaaae', 50)

    assert h.get('aaaae') == 50
    assert str(h) == "[('aaaaa', 10), None, None, None, ('aaaae', 50)]"


def test_get_after_replace():
    h = create_hashmap()

    assert h.set('aaaaa', 100) == 10

    assert h.get('aaaaa') == 100
    assert str(h) == "[('aaaaa', 100), None, None, None, None]"


def test_get_after_wrap_around():
    h = HashDict()

    assert h.set('aaaae', 50) is None
    assert h.set('aaaaa', 10) is None

    assert str(h) == "[('aaaaa', 10), None, None, None, ('aaaae', 50)]"

    h.set('aaaaj', 500)

    assert str(h) == "[('aaaaa', 10), ('aaaaj', 500), None, None, ('aaaae', 50)]"

    assert h.get('aaaaj') == 500

def test_get_after_remove():
    h = create_hashmap()

    assert h.remove('aaaaa') == 10
    assert h.get('aaaaa') is None
    assert str(h) == "[None, None, None, None, None]"


def test_smoke_remove():
    h = create_hashmap()

    h.set('aaaab', 20)

    assert h.remove('aaaaa') == 10
    assert str(h) == "[None, ('aaaab', 20), None, None, None]"


def test_remove_from_not_initialized():
    h = HashDict()

    assert str(h) == "None"
    assert h.remove('any') is None


def test_remove_from_empty():
    h = create_hashmap()

    assert h.remove('aaaaa') == 10

    assert str(h) == "[None, None, None, None, None]"


def test_remove_after_replace():
    h = create_hashmap()

    assert h.set('aaaaa', 100) == 10
    assert h.remove('aaaaa') == 100
    assert str(h) == "[None, None, None, None, None]"


def test_remove_after_rehash():
    h = create_hashmap()

    h.set('aaaab', 20)
    h.set('aaaae', 50)
    h.set('aaaag', 70)

    assert str(h) == "[('aaaaa', 10), ('aaaab', 20), None, None, ('aaaae', 50), None, ('aaaag', 70)]"

    assert h.remove('aaaaa') == 10
    assert str(h) == "[None, ('aaaab', 20), None, None, ('aaaae', 50), None, ('aaaag', 70)]"


def test_compare_equals_both_not_initialized():
    h1 = HashDict()
    assert str(h1) == str(None)

    h2 = HashDict()
    assert h1 == h2


def test_compare_equals_both_empty():
    h1 = create_hashmap()

    h2 = create_hashmap()

    assert h1.remove('aaaaa') == 10
    assert h2.remove('aaaaa') == 10

    assert str(h1) == str(h2)


def test_compare_equals():
    h1 = create_hashmap()

    h2 = create_hashmap()

    assert h1 == h2
    assert str(h1) == "[('aaaaa', 10), None, None, None, None]"


def test_compare_equals_with_different_capacity():
    h1 = create_hashmap()

    h1.set('aaaab', 20)
    h1.set('aaaac', 30)
    h1.set('aaaad', 40)

    assert h1.remove('aaaad') == 40

    assert str(h1) == "[('aaaaa', 10), ('aaaab', 20), ('aaaac', 30), None, None, None, None]"

    h2 = create_hashmap()
    h2.set('aaaab', 20)
    h2.set('aaaac', 30)
    h2.set('aaaad', 40)

    assert h1 == h2


def test_compare_not_equals():
    h1 = create_hashmap()

    h2 = create_hashmap()
    h2.set('aaaab', 20)

    assert not h1 == h2
    assert str(h2) == "[('aaaaa', 10), ('aaaab', 20), None, None, None]"


def test_iter():
    h = create_hashmap()
    h.set('aaaab', 20)
    h.set('aaaac', 30)
    h.set('aaaad', 40)

    ans = HashDict()

    for elem in h:
        if elem is not None:
            # ans.set(key, value)
            ans.set(elem[0], elem[1])

    assert ans == h
