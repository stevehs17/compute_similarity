from typing import Collection, List

def at_least(value: [float, int], minimum: [float, int]) -> [float, int]:
    not_none(value)
    not_none(minimum)
    if value >= minimum:
        return value
    raise ValueError(f'value = {value} less than minimum = {minimum}')

def empty_not_in(c: Collection) -> Collection:
    not_empty(c)
    if None in c or '' in c:
        raise ValueError('has empty or None')
    return c

def more_than(value: [float, int], lower_bound: [float, int]) -> [float, int]:
    not_none(value)
    not_none(lower_bound)
    if value > lower_bound:
        return value
    raise ValueError(f'value = {value} not greater than lower bound = {lower_bound}')

def in_range(value: [float, int], minimum: [float, int], maximum: [float, int]) -> [float, int]:
    not_more_than(minimum, maximum)
    at_least(value, minimum)
    not_more_than(value, maximum)
    return value

def is_equal(value: [float, int, List[str]], target: [float, int]) -> [float, int, List[str]]:
    not_none(value)
    not_none(target)
    if value == target:
        return value
    raise ValueError(f'value={value} not equal to target={target}')

def not_empty(c: [Collection, str]) -> [Collection, str]:
    not_none(c)
    if len(c) > 0:
        return c
    raise ValueError('Object is 0-length')

def not_more_than(value: [float, int], maximum: [float, int]) -> [float, int]:
    not_none(value)
    not_none(maximum)
    if value <= maximum:
        return value
    raise ValueError(f'value = {value} greater than maximum = {maximum}')

def not_none(o: object) -> object:
    if o is None:
        raise ValueError('Object is None')
    return o

