import hw2

''' Returns the set of characters that appear more than k times in
the input string, along with their number of occurrences.
'''


def test_common_chars():
    assert(hw2.common_chars('Mississippi', 1)  ==
    set([('i', 4),  ('p', 2), ('s', 4)]))


def test_mississippi_for_2():
    assert(hw2.common_chars('Mississippi', 2) ==
    set([('i', 4), ('s', 4)]))


def test_empty():
    assert(hw2.common_chars('', 3) == set([])) 


def test_none():
    assert(hw2.common_chars(None, 0) == None)
