from src.algorithms.string_matching.rabin_karp import RabinKarpMatcher
import unittest


class TestRabinKarpMatcher(unittest.TestCase):
    def test_none_string(self):
        matcher = RabinKarpMatcher()

        text = "test text string"
        pattern = None
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = []

        self.assertEqual(results, expected)

    def test_empty_string(self):
        matcher = RabinKarpMatcher()

        text = "abc"
        pattern = ""
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [0, 1, 2, 3]

        self.assertEqual(results, expected)

    def test_simple_single_match(self):
        matcher = RabinKarpMatcher()

        text = "abcdefg"
        pattern = "def"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [3]

        self.assertEqual(results, expected)

    def test_single_match(self):
        matcher = RabinKarpMatcher()

        text = "ababa"
        pattern = "baba"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [1]

        self.assertEqual(results, expected)

    def test_double_match(self):
        matcher = RabinKarpMatcher()

        text = "ababa"
        pattern = "ba"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [1, 3]

        self.assertEqual(results, expected)

    def test_same_character(self):
        matcher = RabinKarpMatcher()

        text = "aaaa"
        pattern = "a"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [0, 1, 2, 3]

        self.assertEqual(results, expected)

    def test_bigger_pattern(self):
        matcher = RabinKarpMatcher()

        text = "aaaa"
        pattern = "lorem ipsum"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = []

        self.assertEqual(results, expected)

    def test_prefix_match(self):
        matcher = RabinKarpMatcher()

        text = "ababaca"
        pattern = "abaca"
        d = 27
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [2]

        self.assertEqual(results, expected)
