import hw2
''' Returns a sorted list containing all of the letters in s1 but not in
s2. This function isn't case sensitive (i.e. 'b' and 'B' are considered
the same letter.) Each distinct letter should appear at most once in
the resulting list, and only letters (a-z, A-Z) will appear in either
string.
'''

def test_ignore_case():
    assert(hw2.free_letters('StrinG', 'struCk') == ['G', 'i', 'n'])


def test_no_duplicated_letter():
    assert(hw2.free_letters('Missisippi', 'mIpPi') == ['s'])


def test_alpha_only():
    assert(hw2.free_letters('Route66', 'out') == ['e', 'R'])
