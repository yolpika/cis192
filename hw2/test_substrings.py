''' Returns a set of all the substrings of s.
'''
import hw2


def test_ab():
    answer = {'', 'a', 'b', 'ab'}
    assert(hw2.substrings('ab') == answer)


def test_abc():
    answer = set(['', 'a', 'b', 'c', 'ab', 'bc', 'abc'])
    assert(hw2.substrings('abc') == answer)


def test_null():
    answer = set([''])
    assert(hw2.substrings('') == answer)


def test_none():
    answer = set()
    assert(hw2.substrings(None) == answer)
