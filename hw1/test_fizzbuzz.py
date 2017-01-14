import hw1


def test_given_3_then_fizzbuzz_return_Fizz():
    assert(hw1.fizzbuzz(3) == 'Fizz')


def test_given_5_then_fizzbuzz_return_Buzz():
    assert(hw1.fizzbuzz(5) == 'Buzz')


def test_given_15_then_fizzbuzz_return_FizzBuzz():
    assert(hw1.fizzbuzz(15) == 'FizzBuzz')


def test_given_16_then_fizzbuzz_does_nothing():
    assert(hw1.fizzbuzz(16) != 'Fizz')
    assert(hw1.fizzbuzz(16) != 'Buzz')
    assert(hw1.fizzbuzz(16) != 'FizzBuzz')
    assert(hw1.fizzbuzz(16) == None)
