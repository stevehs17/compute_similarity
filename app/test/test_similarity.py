from numpy import array
from similarity import compute_pair_similarity, compute_similarity, _get_model, MIN_SIMILARITY, MAX_SIMILARITY
from unittest import mock, TestCase
from util import log

class SimilarityTest(TestCase):
    def test_compute_pair_similarity_success(self):
        log()
        cases = (
            (('I walk', 'I walk'), 0.9999999403953552),
            (('I walk', 'He fell hard'), 0.20952434837818146),
            (('Get the facts.', "Hi Frank, it's Bob."), 0.0),
        )
        for args, out in cases:
            self.assertEqual(out, compute_pair_similarity(*args))

    def test_compute_pair_similarity_bad_args_failure(self):
        log()
        args = (
            (None, 'a'),
            ('', 'a'),
            ('a', None),
            ('a', '')
        )
        for a in args:
            with self.assertRaises(ValueError):
                compute_pair_similarity(*a)

    def test_compute_similarity_success(self):
        log()
        cases = (
            (['I walk'], [[1.0]]),
            (['I walk', 'I walk'], [[0.9999999403953552, 0.9999999403953552], [0.9999999403953552, 0.9999999403953552]]),
            (['I walk', 'He fell hard'], [[0.9999999403953552, 0.20952434837818146], [0.20952434837818146, 1.0]]),
            (["Get the facts.", "Hi Frank, it's Bob."], [[0.9999999403953552, 0.0], [0.0, 1.0]]),

            (['I walk', 'I walk', 'He fell hard'],
                [[1.0, 1.0, 0.20952430367469788],
                 [1.0, 1.0, 0.20952430367469788],
                 [0.20952430367469788, 0.20952430367469788, 1.0]])
        )
        for arg, out in cases:
            self.assertEqual(out, compute_similarity(arg))

    def test_get_similarity_bad_args_failure(self):
        log()
        args = (None, [], ['a', ''], ['a', None])
        for a in args:
            with self.assertRaises(ValueError):
                compute_similarity(a)

    def test__get_model(s):
        s.assertIsNotNone(_get_model())

    def test_negations(s):
        t = 'This is a good role for you'

        u0 = 'Jackie, please take on this role'
        u0n = 'Jackie, please don’t take on this role'

        u1 = "Jackie, you’re a good fit for this role."
        u1n = "Jackie, you’re a poor fit for this role."

        u2 = "Jackie, you would be a good fit for this role."
        u2n = "Jackie, you wouldn’t be a good fit for this role."

        sim0 = compute_pair_similarity(t, u0)
        print('sim u0 =', sim0)
        sim0n = compute_pair_similarity(t, u0n)
        print('sim u0n =', sim0n)
        print('\n')

        sim1 = compute_pair_similarity(t, u1)
        print('sim u1 =', sim1)
        sim1n = compute_pair_similarity(t, u1n)
        print('sim u1n =', sim1n)
        print('\n')

        sim2 = compute_pair_similarity(t, u2)
        print('sim u2 =', sim2)
        sim2n = compute_pair_similarity(t, u2n)
        print('sim u2n =', sim2n)


