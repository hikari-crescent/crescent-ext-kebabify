from __future__ import annotations

from crescent.internal import Includable, AppCommandMeta

import string
import itertools

def _split_pascal_case(s: str) -> list[str]:
    word_breaks: list[int] = []

    for index, (maybe_lower, maybe_upper) in enumerate(itertools.pairwise(s)):
        if maybe_lower in string.ascii_lowercase and maybe_upper in string.ascii_uppercase:
            word_breaks.append(index)

    if not word_breaks:
        return [s]

    words: list[str] = []
    for start, end in itertools.pairwise(itertools.chain([-1], word_breaks, [len(s)-1])):
        words += [s[start+1:end+1]]

    return words

def _split_words(s: str) -> list[str]:

    words = _split_pascal_case(s)

    out = []
    for word in words:
        out += word.split("_")

    return out

def ify_string(s: str) -> str:
    return '-'.join(word.lower() for word in _split_words(s))


def ify(includable: Includable[AppCommandMeta]) -> Includable[AppCommandMeta]:
    includable.metadata.app_command.name = ify_string(includable.metadata.app_command.name)
    return includable
