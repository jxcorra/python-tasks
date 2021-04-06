import doctest
import typing


def to_dividers(number: int) -> typing.List[int]:
    """
    Returns list of dividers for `number`
    >>> to_dividers(12)
    [1, 2, 2, 3]
    >>> to_dividers(11)
    [1, 11]
    >>> to_dividers(15)
    [1, 3, 5]
    """
    assert isinstance(number, int)

    starting_point = 2  # number always can be divided by 1 and itself
    dividers = [1]

    divider = starting_point
    while divider <= number:
        if number % divider == 0:
            dividers.append(divider)
            number //= divider
            divider = starting_point
            continue

        divider += 1

    return dividers


if __name__ == '__main__':
    doctest.testmod()
