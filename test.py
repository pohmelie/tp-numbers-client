from numbers_client import get_number, NumberType, NumberNotFoundType


def compare_partial(full, subset):
    for k, v in subset.items():
        assert k in full
        assert full[k] == v


def test_simple():
    data = get_number(1)
    compare_partial(
        data,
        {
            "found": True,
            "number": 1,
            "type": "trivia",
        },
    )
    assert data["text"]


def test_number_type():
    data = get_number(1, type=NumberType.year)
    compare_partial(
        data,
        {
            "found": True,
            "number": 1,
            "type": "year",
        },
    )
    assert data["text"]


def test_not_found():
    data = get_number(314159265358979)
    compare_partial(
        data,
        {
            "found": False,
            "number": 314159265358979,
            "type": "trivia",
        },
    )
    assert data["text"]

    data = get_number(314159265358979, notfound=NumberNotFoundType.floor)
    compare_partial(
        data,
        {
            "found": False,
            "number": "5500000000000000",
            "type": "trivia",
        },
    )
    assert data["text"]


def test_fragment():
    data = get_number(1, fragment=True)
    compare_partial(
        data,
        {
            "found": True,
            "number": 1,
            "type": "trivia",
        },
    )
    assert data["text"]


def test_default():
    text = "testing default text"
    data = get_number(314159265358979, default=text)
    compare_partial(
        data,
        {
            "found": False,
            "number": 314159265358979,
            "type": "trivia",
            "text": text,
        },
    )


def test_min_max():
    data = get_number("random", min=1, max=100)
    compare_partial(
        data,
        {
            "found": True,
            "type": "trivia",
        },
    )
    assert 1 <= data["number"] <= 100
