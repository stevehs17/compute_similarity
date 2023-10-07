from unittest import TestCase
from util import has_only_word, log, strip_final_punctuation


class UtilTest(TestCase):
    def test_has_only_word_success(s):
        log()
        cases = (
            (('a', ['']), False),
            (('a', ['a']), True),
            (('a', ['b']), False),
            (('a', ['b', 'a']), False),
            (('a', ['a', 'a']), True),
        )
        for args, out in cases:
            s.assertEqual(out, has_only_word(*args))

    def test_has_only_word_bad_arg_failure(s):
        log()
        word = 'a'
        words = ['a']
        args = (
            (None, words),
            ('', words),
            (word, None),
            (word, [])
        )
        for a in args:
            with s.assertRaises(ValueError):
                has_only_word(*a)

    def test_log_success(s):
        name = 'test_log'
        s.assertIn(name, log())

    def test_strip_final_punctuation_success(s):
        log()
        cases = (
            ('a.', 'a'),
            ('a?', 'a'),
            ('a!', 'a'),
            ('.a?b!c!', '.a?b!c' )
        )
        for arg, out in cases:
            s.assertEqual(out, strip_final_punctuation(arg))

    def test_strip_final_punctuation_failure(s):
        log()
        args = (None, '', '.', '?', '!')
        for a in args:
            with s.assertRaises(ValueError):
                strip_final_punctuation(a)



