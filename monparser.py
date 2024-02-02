from typing import Callable, TypeVar


A = TypeVar("A")
B = TypeVar("B")
Result = list[tuple[A, str]]
Parser = Callable[[str], Result[A]]


def result(v: A) -> Parser[A]:
    return lambda inp: [(v, inp)]


def zero() -> Parser[A]:
    return lambda _: []


def item() -> Parser[str]:
    def item_parser(inp: str) -> Result[str]:
        if inp == "":
            return []
        else:
            return [(inp[0], inp[1:])]

    return item_parser


def seq(p: Parser[A], q: Parser[B]) -> Parser[tuple[A, B]]:
    def seq_parser(inp: str) -> Result[tuple[A, B]]:
        return [((v, w), inp2) for (v, inp1) in p(inp) for (w, inp2) in q(inp1)]

    return seq_parser


def bind(p: Parser[A], f: Parser[B]) -> Parser[B]:
    def bind_parser(inp: str) -> Result[B]:
        return [w for (v, inp1) in p(inp) for w in f(v)(inp1)]

    return bind_parser


def seq2(p: Parser[A], q: Parser[B]) -> Parser[tuple[A, B]]:
    return bind(p, lambda x: bind(q, lambda y: result((x, y))))


def sat(p: Callable[[str], bool]) -> Parser[str]:
    return bind(item(), lambda x: result(x) if p(x) else zero())


def char(x: str) -> Parser[str]:
    return sat(lambda y: x == y)


def digit() -> Parser[str]:
    return sat(lambda x: '0' <= x <= '9')


def lower() -> Parser[str]:
    return sat(lambda x: 'a' <= x <= 'z')


def upper() -> Parser[str]:
    return sat(lambda x: 'A' <= x <= 'Z')
