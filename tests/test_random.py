from unordereddict import UnorderedDict


def test_iter():
    ud = UnorderedDict(a=1, b=2, c=3)
    s = set()
    for _ in range(100):
        s.add(tuple(ud))

    assert s == {
        ('a', 'b', 'c'),
        ('a', 'c', 'b'),
        ('b', 'a', 'c'),
        ('b', 'c', 'a'),
        ('c', 'a', 'b'),
        ('c', 'b', 'a'),
    }


def test_keys():
    ud = UnorderedDict(a=1, b=2, c=3)
    s = set()
    for _ in range(100):
        s.add(tuple(ud.keys()))

    assert s == {
        ('a', 'b', 'c'),
        ('a', 'c', 'b'),
        ('b', 'a', 'c'),
        ('b', 'c', 'a'),
        ('c', 'a', 'b'),
        ('c', 'b', 'a'),
    }


def test_values():
    ud = UnorderedDict(a=1, b=2, c=3)
    s = set()
    for _ in range(100):
        s.add(tuple(ud.values()))

    assert s == {
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    }


def test_items():
    ud = UnorderedDict(a=1, b=2, c=3)
    s = set()
    for _ in range(100):
        s.add(tuple(ud.items()))

    assert s == {
        (('a', 1), ('b', 2), ('c', 3)),
        (('a', 1), ('c', 3), ('b', 2)),
        (('b', 2), ('a', 1), ('c', 3)),
        (('b', 2), ('c', 3), ('a', 1)),
        (('c', 3), ('a', 1), ('b', 2)),
        (('c', 3), ('b', 2), ('a', 1)),
    }


def test_popitem():
    s = set()
    for _ in range(100):
        ud = UnorderedDict(a=1, b=2, c=3)
        s.add(ud.popitem())
        while ud:
            ud.popitem()

    assert s == {('a', 1), ('b', 2), ('c', 3)}
