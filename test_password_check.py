from password_check import password_verification
import pytest


test_cases_psw_check = [
    ('Bb+jkwcnwї88', False),
    ('ї', False),
    (' ', False),
    ('Bb+jkwcnw88', True),
    ('Bb+jkwcnw', False),
    ('Bbjkwcnw88', False),
    ('b+jkwcnw88', False),
    ('Bb+jkwcnw88 ', False),
]


@pytest.mark.parametrize('value, expected', test_cases_psw_check)
def test_password_verification(value, expected):
    processed = password_verification(value)
    assert processed == expected


    # value = 'ц'
    # expected = 'w'
    # assert value == expected
    # value = 'у'
    # expected = 'e'
    # assert value == expected
    # value = 'к'
    # expected = 'r'
    # assert value == expected
    # value = 'е'
    # expected = 't'
    # assert value == expected
    # value = 'н'
    # expected = 'y'
    # assert value == expected
    # value = 'г'
    # expected = 'u'
    # assert value == expected
    # value = 'ш'
    # expected = 'i'
    # assert value == expected
    # value = 'щ'
    # expected = 'o'
    # assert value == expected
    # value = 'з'
    # expected = 'p'
    # assert value == expected
    # value = 'х'
    # expected = '['
    # assert value == expected
    # value = 'ї'
    # expected = ']'
    # assert value == expected
    # value = 'ф'
    # expected = 'a'
    # assert value == expected
    # value = 'і'
    # expected = 's'
    # assert value == expected
    # value = 'в'
    # expected = 'd'
    # assert value == expected
    # value = 'а'
    # expected = 'f'
    # assert value == expected
    # value = 'п'
    # expected = 'g'
    # assert value == expected
    # value = 'р'
    # expected = 'h'
    # assert value == expected
    # value = 'о'
    # expected = 'j'
    # assert value == expected
    # value = 'л'
    # expected = 'k'
    # assert value == expected
    # value = 'д'
    # expected = 'l'
    # assert value == expected
    # value = 'ж'
    # expected = ';'
    # assert value == expected
    # value = 'є'
    # expected = '"'
    # assert value == expected
    # value = 'я'
    # expected = 'z'
    # assert value == expected
    # value = 'ч'
    # expected = 'x'
    # assert value == expected
    # value = 'с'
    # expected = 'c'
    # assert value == expected
    # value = 'м'
    # expected = 'v'
    # assert value == expected
    # value = 'и'
    # expected = 'b'
    # assert value == expected
    # value = 'т'
    # expected = 'n'
    # assert value == expected
    # value = 'ь'
    # expected = 'm'
    # assert value == expected
    # value = 'б'
    # expected = ','
    # assert value == expected
    # value = 'ю'
    # expected = '.'
    # assert value == expected


