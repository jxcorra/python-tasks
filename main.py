def print_hello(name):
    print('Hello ' + name)


def is_even(number):
    return number % 2 == 0


def is_all_less_than(sequence, bound):
    return all(item < bound for item in sequence)
