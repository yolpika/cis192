import hw2


def test_abcdefg_gfedcba():
    assert(hw2.are_anagrams('abcdefg', 'gfedcba') == True)


def test_holycow_wolycoh():
    assert(hw2.are_anagrams('holycow', 'wolycoh') == False)
