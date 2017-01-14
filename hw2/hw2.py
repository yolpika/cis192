""" Homework 2
-- Due Sunday, September 18th at 23:59
-- Before starting, read
https://www.cis.upenn.edu/~cis192/homework/
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""


def free_letters(s1, s2):
    ''' Returns a sorted list containing all of the letters in s1 but not in
    s2. This function isn't case sensitive (i.e. 'b' and 'B' are considered
    the same letter.) Each distinct letter should appear at most once in
    the resulting list, and only letters (a-z, A-Z) will appear in either
    string.
    '''
    extracted_list = [x for x in s1 if x.upper() not in s2.upper()]
    numbers = [str(n) for n in range(0, 10)]

    temp = set(extracted_list) - set(numbers)
    result = sorted(temp, key=str.lower)

    return list(result)


def substrings(s):
    ''' Returns a set of all the substrings of s.
    '''
    result = set([])
    if s is not None:
        for length_to_pick in range(0, len(s) + 1):
            for start_index in range(0, len(s) + 1):
                substring = s[start_index:start_index + length_to_pick]
                result.add(substring)

    return result


def common_chars(s, k):
    ''' Returns the set of characters that appear more than k times in
    the input string, along with their number of occurrences.
    '''
    if s is None:
        return None

    hist = {}
    for c in s:
        if c not in hist:
            hist[c] = 1
        else:
            hist[c] += 1

    result = [(key, value) for key, value in hist.items() if value > k]
    return set(result)


def are_anagrams(s1, s2):
    ''' Returns True if strings s1 and s2 are anagrams, and False otherwise.
    '''
    l = [c for c in s1]
    l.reverse()
    result = ''.join(l) == s2

    return result


def my_sort(lst):
    ''' Return a sorted copy of a list. Do not modify the original list. Do
    not use Python's built in sorted method or [].sort(). You may use
    any sorting algorithm of your choice (mergesort or quicksort recommended.)
    '''
    pass


def my_permute(lst):
    ''' Returns a list of all permutations of a list. Do not use any of
    Python's builtin functions from the itertools library. Sort the list
    using my_sort before returning it, and remove any duplicates as well.
    Note that the set() trick won't work right off the bat -- why not?
    '''
    def find_largest_k(a):
        k = -1
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                if i > k:
                    k = i
        return k

    def find_largest_l(a, k):
        l = 0
        for i in range(0, len(a)):
            if a[k] < a[i]:
                if i > l:
                    l = i
        return l

    result = []
    result.append(lst.copy())
    while True:
        k = find_largest_k(lst)
        if k == -1:
            break
        l = find_largest_l(lst, k)
        lst[k], lst[l] = lst[l], lst[k]
        tmp = lst[k + 1:]
        tmp.reverse()
        lst[k + 1:] = tmp
        result.append(lst.copy())

    return sorted(result)


def main():
    pass

if __name__ == "__main__":
    main()
