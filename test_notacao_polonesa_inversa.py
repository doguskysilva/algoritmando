from notacao_polonesa_inversa import (
    notacao_polonesa_inversa,
    organiza_expressao,
    calcula_notacao_expressao_polonesa_inversa,
    ordem_precedencia_eh_maior,
)
import pytest


@pytest.mark.parametrize(
    "procedencia_atual,procedencia_stack,expected",
    [
        ("+", "-", False),
        ("+", "*", False),
        ("+", "^", False),
        ("*", "+", True),
        ("*", "/", False),
        ("^", "*", True),
    ],
)
def test_ordens_precedencia_das_operacoes(
    procedencia_atual, procedencia_stack, expected
):
    assert ordem_precedencia_eh_maior(procedencia_atual, procedencia_stack) == expected


@pytest.mark.parametrize(
    "expressao,expected",
    [
        ("A*B", "A * B"),
        ("A *B/2", "A * B / 2"),
        ("a+b*(c^d-e)^(f+g*h)-i", "a + b * ( c ^ d - e ) ^ ( f + g * h ) - i"),
        ("  (4 + (7 * 4)) + 12 /3", "( 4 + ( 7 * 4 ) ) + 12 / 3"),
        ("4 - (1+2*3)/ 4 ", "4 - ( 1 + 2 * 3 ) / 4"),
        ("(A+B) * (C-D)", "( A + B ) * ( C - D )")
    ],
)
def test_organiza_expressao(expressao, expected):
    assert organiza_expressao(expressao) == expected

@pytest.mark.parametrize(
    "expressao,expected",
    [
        ("A*B", ["A", "B", "*"]),
        ("A *B/2", ["A", "B", "*", "2", "/"]),
        ("a+b*(c^d-e)^(f+g*h)-i", ["a", "b", "c", "d", "^", "e", "-", "f", "g", "h", "*", "+", "^", "*", "+", "i", "-"]),
        ("(4 + (7 * 4)) + 12 /3", ["4", "7", "4", "*", "+", "12", "3", "/", "+"]),
        ("(A+B) * (C-D)", ["A", "B", "+", "C", "D", "-", "*"])
    ],
)
def test_notacao_polonesa_inversa(expressao, expected):
    assert notacao_polonesa_inversa(expressao) == expected

@pytest.mark.parametrize(
    "expressao, expected",
    [
        ("3*3", 9)
    ]
)
def test_calcula_notacao_expressao_polonesa_inversa(expressao, expected):
    assert calcula_notacao_expressao_polonesa_inversa(expressao) == expected