from pollards_rho.pollards_rho import PollardsRho
import pytest


def test_composite_number():
    num = 20701  # 163 * 127
    factor = PollardsRho(num).factorize()

    assert num % factor == 0
    assert factor not in [1, num]  # factor should be non-trivial


def test_prime_number():
    num = 13
    factor = PollardsRho(num).factorize()

    assert factor == num


def test_negative_number():
    with pytest.raises(ValueError):
        PollardsRho(0).factorize()


def test_even_number():
    num = 2048
    factor = PollardsRho(num).factorize()

    assert factor == 2


def test_zero():
    with pytest.raises(ValueError):
        PollardsRho(0).factorize()


def test_one():
    num = 1
    factor = PollardsRho(num).factorize()

    assert factor == 1


def test_large_composite_number():
    num = 488012747 * 832406063
    factor = PollardsRho(num).factorize()

    assert num % factor == 0
    assert factor not in [1, num]  # factor should be non-trivial
