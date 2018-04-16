"""Test basic mapping capabilities of UnorderedDict.

UnorderedDict is a subclass of UserDict, so let's make sure that it fulfills all UserDict's obligations.
"""
from test.test_userdict import UserDictTest

from unordereddict import UnorderedDict


class TestUserDict(UserDictTest):
    """Test class that tests UnorderedDict."""
    type2test: type = UnorderedDict

    def test_popitem(self) -> None:
        """Test popitem."""
        d = self._empty_mapping()
        self.assertRaises(KeyError, d.popitem)
        self.assertRaises(TypeError, d.popitem, 42)

    def test_repr(self) -> None:
        """Test UnorderedDict representation."""
        d = self._empty_mapping()
        self.assertEqual(repr(d), 'UnorderedDict({})')
        d[1] = 2
        self.assertEqual(repr(d), 'UnorderedDict({1: 2})')
        d = self._empty_mapping()
        d[1] = d
        self.assertEqual(repr(d), 'UnorderedDict({1: UnorderedDict({...})})')

        class Exc(Exception):
            pass

        class BadRepr(object):
            def __repr__(self):
                raise Exc()

        d = self._full_mapping({1: BadRepr()})
        self.assertRaises(Exc, repr, d)
