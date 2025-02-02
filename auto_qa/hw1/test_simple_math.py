from simple_math import SimpleMath
import pytest


@pytest.fixture
def simple_math():
    return SimpleMath()


@pytest.mark.parametrize(
    'x, expected_result',
    [
        (0, 0),
        (2, 4),
        (-3, 9),
    ]
)
def test_square(simple_math, x, expected_result):
    assert simple_math.square(x) == expected_result


@pytest.mark.parametrize(
    'x, expected_result',
    [
        (0, 0),
        (2, 8),
        (-3, -27),
    ]
)
def test_cube(simple_math, x, expected_result):
    assert simple_math.cube(x) == expected_result
