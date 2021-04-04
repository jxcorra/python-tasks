import doctest
import re
from typing import Optional


def get_safe_if(from_str: str, regexp: str, group: Optional[int] = None) -> Optional[str]:
    """
    Returns matched `group` (optional) or match from `from_str` specified by `regexp`
    >>> get_safe_if('abc', 'qwe')
    >>> get_safe_if('abc', 'qwe', 1)
    >>> get_safe_if('abc', 'a(bc)', 1)
    'bc'
    >>> get_safe_if('abc', 'a(bc)')
    'abc'
    """
    if match := re.search(regexp, from_str):
        return match.group(group or 0)

    return None


def get_safe_exc(from_str: str, regexp: str, group: Optional[int] = None) -> Optional[str]:
    """
    Returns matched `group` (optional) or match from `from_str` specified by `regexp`
    >>> get_safe_exc('abc', 'qwe')
    >>> get_safe_exc('abc', 'qwe', 1)
    >>> get_safe_exc('abc', 'a(bc)', 1)
    'bc'
    >>> get_safe_exc('abc', 'a(bc)')
    'abc'
    """
    try:
        return re.search(regexp, from_str).group(group or 0)
    except AttributeError:
        return None


if __name__ == '__main__':
    doctest.testmod()
