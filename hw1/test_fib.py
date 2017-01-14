import hw1


def test_fib_iter_1_is_0():
    assert(hw1.fib_iter(1) == 0)


def test_fib_iter_2_is_1():
    assert(hw1.fib_iter(2) == 1)


def test_fib_iter_3_is_1():
    assert(hw1.fib_iter(3) == 1)


def test_fib_iter_7_is_8():
    assert(hw1.fib_iter(7) == 8)


def test_fib_rec_1_is_0():
    assert(hw1.fib_rec(1) == 0)


def test_fib_rec_2_is_1():
    assert(hw1.fib_rec(2) == 1)


def test_fib_rec_3_is_1():
    assert(hw1.fib_rec(3) == 1)


def test_fib_rec_7_is_8():
    assert(hw1.fib_rec(7) == 8)
