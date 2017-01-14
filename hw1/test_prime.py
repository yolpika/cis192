import hw1


def test_1_is_not_prime():
    result = hw1.is_prime(1)
    assert(result, False)


def test_101_is_prime():
    assert(hw1.is_prime(101))


def test_503_is_prime():
    assert(hw1.is_prime(503))


def test_is_prime_gen():
    plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,
             47,53,59,61,67,71,73,79,83,89,97,101,
             103,107,109,113]
    for n in plist:
        assert(hw1.is_prime(n))


def test_4_is_not_prime():
    assert(hw1.is_prime(4) == False)


def test_200_is_not_prime():
    assert(hw1.is_prime(200) == False)


def test_first_prime_is_2():
    assert(hw1.nth_prime(1) == 2)


def test_third_prime_is_5():
    assert(hw1.nth_prime(3) == 5)


def test_anon_prime():
    plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,
             47,53,59,61,67,71,73,79,83,89,97,101,
             103,107,109,113]

    ilist = [i for i in range(1, len(plist))]
    for i in ilist:
        assert(hw1.nth_prime(i) == plist[i - 1])
