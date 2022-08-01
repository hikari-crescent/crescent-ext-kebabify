from crescent.ext import kebab


def test_pascal_case():
    assert kebab._split_pascal_case("TestingPascalCase") == [
        "Testing",
        "Pascal",
        "Case",
    ]


def test_snake_case():
    assert kebab._split_snake_case("testing_snake_case") == ["testing", "snake", "case"]


def test_split_words():
    assert kebab.split_words("TestSplit_words") == ["Test", "Split", "words"]


def test_override_no_functions():
    assert kebab.split_words("TestSplit_words", override=True) == ["TestSplit_words"]


def test_override_with_functions():
    assert kebab.split_words(
        "TestSplit_words", override=True, split_functions=[kebab._split_pascal_case]
    ) == ["Test", "Split_words"]


def test_extend_split_functions():
    CALLED = False

    def custom_split(s: str) -> list[str]:
        nonlocal CALLED
        CALLED = True
        return [s]

    assert kebab.split_words("TestSplit_words", split_functions=[custom_split]) == [
        "Test",
        "Split",
        "words",
    ]
    assert CALLED
