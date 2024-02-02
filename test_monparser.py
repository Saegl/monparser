from monparser import *


def test_result() -> None:
    parser = result("Alisher")
    output = parser("something")
    assert output == [("Alisher", "something")]


def test_zero() -> None:
    parser: Parser[str] = zero()
    output = parser("something")
    assert output == []


def test_item() -> None:
    parser = item()
    output = parser("Alisher")
    assert output == [("A", "lisher")]


def test_seq() -> None:
    parser1: Parser[str] = result("Hello")
    parser2: Parser[int] = result(42)

    seq_parser = seq2(parser1, parser2)

    output = seq_parser("World")
    assert output == [(("Hello", 42), "World")]


def test_char() -> None:
    parser = char("a")

    output = parser("alisher")
    assert output == [("a", "lisher")]

    output = parser("bekzat")
    assert output == []


def test_upper() -> None:
    parser = upper()

    output = parser("Alisher")
    assert output == [("A", "lisher")]

    output = parser("alisher")
    assert output == []


def test_two() -> None:
    parser = bind(lower(), lambda x: bind(lower(), lambda y: result(x + y)))

    output = parser("abcde")
    assert output == [("ab", "cde")]
