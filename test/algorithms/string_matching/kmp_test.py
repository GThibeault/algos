from src.algorithms.string_matching.kmp import KnuthMorrisPrattMatcher
import unittest


class TestKMPMatcher(unittest.TestCase):
    def test_none_string(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "test text string"
        pattern = None

        results = matcher.match(text, pattern)
        expected = []

        self.assertEqual(results, expected)

    def test_empty_string(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "abc"
        pattern = ""

        results = matcher.match(text, pattern)
        expected = [0, 1, 2, 3]

        self.assertEqual(results, expected)

    def test_simple_single_match(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "abcdefg"
        pattern = "def"

        results = matcher.match(text, pattern)
        expected = [3]

        self.assertEqual(results, expected)

    def test_single_match(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "ababa"
        pattern = "baba"

        results = matcher.match(text, pattern)
        expected = [1]

        self.assertEqual(results, expected)

    def test_double_match(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "ababa"
        pattern = "ba"

        results = matcher.match(text, pattern)
        expected = [1, 3]

        self.assertEqual(results, expected)

    def test_same_character(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "aaaa"
        pattern = "a"

        results = matcher.match(text, pattern)
        expected = [0, 1, 2, 3]

        self.assertEqual(results, expected)

    def test_bigger_pattern(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "aaaa"
        pattern = "lorem ipsum"

        results = matcher.match(text, pattern)
        expected = []

        self.assertEqual(results, expected)

    def test_prefix_match(self):
        matcher = KnuthMorrisPrattMatcher()

        text = "ababaca"
        pattern = "abaca"

        results = matcher.match(text, pattern)
        expected = [2]

        self.assertEqual(results, expected)
