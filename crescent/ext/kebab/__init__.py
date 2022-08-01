from __future__ import annotations

from itertools import pairwise

import typing


if typing.TYPE_CHECKING:
    from crescent.internal import Includable, AppCommandMeta


def _split_pascal_case(s: str) -> list[str]:
    word_breaks: list[int] = []

    for index, (maybe_lower, maybe_upper) in enumerate(pairwise(s)):
        if maybe_lower.islower() and maybe_upper.isupper():
            word_breaks.append(index + 1)

    if not word_breaks:
        return [s]

    words: list[str] = []
    for start, end in pairwise([0, *word_breaks, len(s)]):
        words.append(s[start:end])

    return words


def _split_snake_case(s: str) -> list[str]:

    words = _split_pascal_case(s)

    out = []
    for word in words:
        out += word.split("_")

    return out


def ify_string(s: str) -> str:
    return "-".join(_split_snake_case(s)).lower()


def ify(includable: Includable[AppCommandMeta]) -> Includable[AppCommandMeta]:
    includable.metadata.app_command.name = ify_string(
        includable.metadata.app_command.name
    )
    return includable
