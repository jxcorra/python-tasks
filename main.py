def print_hello(name):
    assert isinstance(name, str)

    print('Hello ' + name)


def is_even(number):
    assert isinstance(number, int)

    return number % 2 == 0


def is_all_less_than(sequence, bound):
    assert all(isinstance(item, int) for item in sequence)

    return all(item < bound for item in sequence)
