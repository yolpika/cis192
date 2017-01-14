import hw1


def test_given_int_then_snapcrackle_return_Crackle():
    assert(hw1.snapcrackle(15) == 'Snap')


def test_given__float_then_snapcrackle_return_nothing():
    assert(hw1.snapcrackle(2.8) != 'Crackle')
    assert(hw1.snapcrackle(3.2) == None)
