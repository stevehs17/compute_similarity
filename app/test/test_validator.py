from util import log
from unittest import TestCase
from validator import at_least, empty_not_in, more_than, in_range, is_equal, not_empty, not_more_than, not_none

class ValidatorTest(TestCase):
    _NUMBERS = (1, 1.0)
    _NON_STRING_SEQUENCES = ([1], {1}, {1: 2}, (1, 2))
    _SEQUENCES = ('a',) + _NON_STRING_SEQUENCES
    _EMPTIES = ('', [], {}, ())

    def test_at_least_success(s):
        log()
        for n in s._NUMBERS:
            s.assertEqual(n, at_least(n, n))

    def test_at_least_failure(s):
        log()
        for n in s._NUMBERS:
            args = (
                (None, n),
                (n, None),
                (n-1, n)
            )
            for a in args:
                with s.assertRaises(ValueError):
                    at_least(*a)

    def test_empty_not_in_success(s):
        log()
        for e in s._NON_STRING_SEQUENCES:
            s.assertEqual(e, empty_not_in(e))

    def test_empty_not_in_failure(s):
        log()
        args = (
            None,
            [None],
            [''],
            ['a', None],
            (None,),
            ('', ),
        )
        for a in args:
            with s.assertRaises(ValueError):
                empty_not_in(a)

    def test_greater_than_success(s):
        log()
        for n in s._NUMBERS:
            s.assertEqual(n, more_than(n, n - 1))

    def test_greater_than_failure(s):
        log()
        for n in s._NUMBERS:
            args = (
                (None, n),
                (n, None),
                (n, n+1)
            )
            for a in args:
                with s.assertRaises(ValueError):
                    more_than(*a)

    def test_in_range_success(s):
        log()
        for n in s._NUMBERS:
            s.assertEqual(n, in_range(n, n, n))

    def test_in_range_failure(s):
        log()
        for n in s._NUMBERS:
            args = (
                (None, n, n),
                (n, None, n),
                (n, n, None),
                (n-1, n, n),
                (n+1, n, n),
                (n, n+1, n),
                (n, n, n-1)
            )
            for a in args:
                with s.assertRaises(ValueError):
                    in_range(*a)

    def test_is_equal_success(s):
        log()
        for n in s._NUMBERS + ('test',):
            s.assertEqual(n, is_equal(n, n))

    def test_is_equal_failure(s):
        log()
        for n in s._NUMBERS:
            args = (
                (None, n),
                (n, None),
                (n, n+1),
                ('test', 'tests')
            )
            for a in args:
                with s.assertRaises(ValueError):
                    is_equal(*a)

    def test_not_empty_success(s):
        log()
        for e in s._SEQUENCES:
            s.assertEqual(e, not_empty(e))

    def test_not_empty_failure(s):
        log()
        for e in (None,) + s._EMPTIES:
            with s.assertRaises(ValueError):
                not_empty(e)

    def test_not_more_than_success(s):
        log()
        for n in s._NUMBERS:
            s.assertEqual(n, not_more_than(n, n))

    def test_not_more_than_failure(s):
        log()
        for n in s._NUMBERS:
            args = (
                (None, n),
                (n, None),
                (n+1, n)
            )
            for a in args:
                with s.assertRaises(ValueError):
                    not_more_than(*a)

    def test_not_none_success(s):
        log()
        for i in s._NUMBERS + s._SEQUENCES + s._EMPTIES:
            s.assertEqual(i, not_none(i))

    def test_not_none_failure(s):
        log()
        with s.assertRaises(ValueError):
            not_none(None)

