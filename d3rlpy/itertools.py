from typing import Iterator, Tuple, TypeVar

__all__ = ["last_flag", "first_flag"]

T = TypeVar("T")


def last_flag(iterator: Iterator[T]) -> Iterator[Tuple[bool, T]]:
    items = list(iterator)
    for i, item in enumerate(items):
        yield i == len(items) - 1, item


def first_flag(iterator: Iterator[T]) -> Iterator[Tuple[bool, T]]:
    items = list(iterator)
    for i, item in enumerate(items):
        yield i == 0, item
