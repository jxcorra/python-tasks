import re
from typing import Optional


class MyOwnException(Exception):
    pass


input_data = 'fc86f9cbcaf64562852294bf21992aa27c5c3e219ce141dd84f0b54348080b34a1defb854542463f88e1b9cd88f31e28'


# спрашиваем разрешения
def get_safe_if(from_str: str, regexp: str, group: Optional[int] = None) -> Optional[str]:
    """Returns matched `group` (optional) or match from `from_str` specified by `regexp`"""
    if match := re.search(regexp, from_str).group(group or 0):
        return match

    return None


digits_after_two_a = (get_safe_if(input_data, r'aa(\d+)', 1))


assert int(digits_after_two_a) == 27


# извиняемся если что-то пошло не так
def get_safe_exc(from_str: str, regexp: str, group: Optional[int] = None) -> Optional[str]:
    """Returns matched `group` (optional) or match from `from_str` specified by `regexp`"""
    try:
        return re.search(regexp, from_str).group(group or 0)
    except AttributeError:
        return None


digits_after_three_a = (get_safe_exc(input_data, r'aaa(\d+)', 1))
assert digits_after_three_a is None


data_without_zeroes = re.sub('0', '', input_data)
assert '0' not in data_without_zeroes
