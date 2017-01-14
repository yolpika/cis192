import hw1
import fractions as fr


def test_gcd_of_12_9_is_3():
    assert(hw1.gcd_iter(12, 9) == fr.gcd(12, 9))
    assert(hw1.gcd_rec(12, 9) == fr.gcd(12, 9))


def test_gcd_of_11_5_is_1():
    assert(hw1.gcd_iter(11, 5) == fr.gcd(11, 5))
    assert(hw1.gcd_rec(11, 5) == fr.gcd(11, 5))


def test_gcs_of_1_2_is_1():
    assert(hw1.gcd_iter(1, 2) == fr.gcd(1, 2))
    assert(hw1.gcd_rec(1, 2) == fr.gcd(1, 2))


def test_gcd_of_64_24_is_8():
    assert(hw1.gcd_iter(64, 24) == fr.gcd(64, 24))
    assert(hw1.gcd_rec(64, 24) == fr.gcd(64, 24))


def test_gcd_of_0_1_is():
    assert(hw1.gcd_iter(0, 1) == fr.gcd(0, 1))
    assert(hw1.gcd_rec(0, 1) == fr.gcd(0, 1))


def test_gcd_of_minus30_minus25_is_minus5():
    assert(hw1.gcd_iter(-30, -25) == fr.gcd(-30, -25))
    assert(hw1.gcd_rec(-30, -25) == fr.gcd(-30, -25))


def test_gcd_of_30_minus25_is_():
    assert(hw1.gcd_iter(30, -25) == fr.gcd(30, -25))
    assert(hw1.gcd_rec(30, -25) == fr.gcd(30, -25))


def test_gcd_of_minus30_minus15_is_minus15():
    assert(hw1.gcd_iter(-30, -15) == fr.gcd(-30, -15))
    assert(hw1.gcd_rec(-30, -15) == fr.gcd(-30, -15))
