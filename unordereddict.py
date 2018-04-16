from collections import UserDict
from random import randrange
from typing import Iterable, Generator, Tuple, Hashable, Any, TypeVar

_A = TypeVar('_A')


def _shuffled(iterable: Iterable[_A]) -> Generator[_A, None, None]:
    """Implementation of `Fisher–Yates shuffle`_.

    .. _`Fisher–Yates shuffle`: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm

    :param iterable: an iterable to shuffle
    :return: a generator that returns elements from the iterable in random order
    """
    lst = list(iterable)
    while lst:
        random_index = randrange(0, len(lst))
        lst[-1], lst[random_index] = lst[random_index], lst[-1]
        yield lst.pop()


class UnorderedDict(UserDict):
    """An implementation of `MutableMapping` that always returns keys, values and items in random order.

    Because of implementation of UserDict we only need to override `__iter__()` method.
    Methods `keys()`, `values()` and `items()` depend on it.
    """
    data: dict  # dict that contains the actual data

    def __iter__(self) -> Generator:
        """Iteration of keys of the dict in random order.

        :return: a generator that iterates keys of the dict in random order
        """
        for key in _shuffled(self.data):
            yield key

    def __repr__(self) -> str:
        """String representation of an instance of UnorderedDict.

        Use wrapped representation of the underlying dict.

        :return: string representation
        """
        return f'UnorderedDict({self.data!r})'

    def popitem(self) -> Tuple[Hashable, Any]:
        """Pop a random item from the mapping.

        :return: key, value
        """
        if len(self.data) <= 1:
            return self.data.popitem()
        random_index = randrange(0, len(self.data))
        dict_iterator = iter(self.data)
        for _ in range(0, random_index - 1):
            next(dict_iterator)
        key = next(dict_iterator)
        return key, self.data.pop(key)
