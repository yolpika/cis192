import unittest
from hw2 import *


class TestHomework2(unittest.TestCase):

    def setUp(self):
        pass

    # free_letters
    def test_free_letters(self):
        self.assertEqual(free_letters('Bond', 'Rambo'), ['d', 'n'])
        self.assertEqual(free_letters('Origami', 'Hydrogen'), ['a', 'i', 'm'])

    # substrings
    def test_substrings(self):
        ans1 = {'', 'a', 'b', 'c', 'ab', 'bc', 'abc'}
        self.assertEqual(substrings('abc'), ans1)
        ans2 = set(['', 'Boris', 'B', 'i', 'Bor', 'Bo', 'ris', 'o', 'ri', 's',
                    'r', 'Bori', 'ori', 'oris', 'or', 'is'])
        self.assertEqual(substrings('Boris'), ans2)

    # common chars
    def test_common_chars(self):
        self.assertEqual(common_chars('hello', 1), {('l', 2)})
        s = '''
        When in the Course of human events, it becomes necessary for one people
        to dissolve the political bands which have connected them with another,
        and to assume among the powers of the earth, the separate and equal
        station to which the Laws of Nature and of Nature's God entitle them,
        a decent respect to the opinions of mankind requires that they should
        declare the causes which impel them to the separation.'''
        ans = set([('n', 22), ('h', 27), ('a', 26), ('d', 11), ('e', 50),
                   (' ', 113), ('r', 14), ('o', 27), ('s', 22), ('c', 12),
                   ('i', 17), ('t', 37)])
        self.assertEqual(common_chars(s, 10), ans)

    # are_anagrams
    def test_anagrams(self):
        self.assertTrue(are_anagrams('abc', 'cba'))
        self.assertFalse(are_anagrams('admired', 'married'))
        self.assertFalse(are_anagrams('generate', 'teenager'))
        self.assertFalse(are_anagrams('apple', 'pear'))

    # my_sort
    def test_my_sort(self):
        l1 = [5, 2, 1, 4, 3]
        self.assertEqual(my_sort(l1), sorted(l1))
        l2 = ['c', 'a', 'b']
        self.assertEqual(my_sort(l2), sorted(l2))

    # my_permute
    def test_my_permute(self):
        ans1 = [['a', 'b'], ['b', 'a']]
        self.assertEqual(my_permute(['a', 'b']), ans1)
        ans2 = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(my_permute([1, 2, 3]), ans2)
        ans3 = [[1, 1]]
        self.assertEqual(my_permute([1, 1]), ans3)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
