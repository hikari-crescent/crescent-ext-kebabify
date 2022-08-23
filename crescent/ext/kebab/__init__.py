from __future__ import annotations
from functools import partial

import typing

SPLIT_TYPE: typing.TypeAlias = typing.Callable[[str], list[str]]


if typing.TYPE_CHECKING:
    from crescent.internal import Includable, AppCommandMeta


def _split_pascal_case(s: str) -> list[str]:
    words = []
    last = 0
    for c, char in enumerate(s):
        if c and char.isupper():
            words.append(s[last:c])
            last = c

    words.append(s[last:])
    return words


def _split_snake_case(s: str) -> list[str]:
    return s.split("_")


def split_words(
    s: str,
    *,
    split_functions: list[SPLIT_TYPE] | None = None,
    override: bool = False,
) -> list[str]:
    if not split_functions:
        split_functions = []

    if not override:
        split_functions.extend([_split_snake_case, _split_pascal_case])

    if not split_functions:
        return [s]

    words = split_functions[0](s)

    def apply_split(words: list[str], func: SPLIT_TYPE) -> list[str]:
        out: list[str] = []
        for word in words:
            out.extend(func(word))
        return out

    for func in split_functions[1:]:
        words = apply_split(words, func)

    return words


def ify_string(
    s: str, *, split_functions: list[SPLIT_TYPE] = None, override: bool = False
) -> str:
    return "-".join(
        split_words(s, split_functions=split_functions, override=override)
    ).lower()


def ify(
    split_functions: list[SPLIT_TYPE],
    override: bool = False,
    includable: Includable[AppCommandMeta] | None = None
) -> Includable[AppCommandMeta]:
    if not includable:
        # honestly do not give enough of a shit to fix this
        return partial(
            ify,
            split_functions=split_functions,
            override=override,
        )  # type: ignore

    includable.metadata.app_command.name = ify_string(
        includable.metadata.app_command.name
    )
    return includable
