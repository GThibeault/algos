from src.algorithms.string_matching.naive import NaiveMatcher
import unittest


class TestNaiveStringMatcher(unittest.TestCase):
    def test_none_string(self):
        matcher = NaiveMatcher()

        text = "test text string"
        pattern = None

        results = matcher.match(text, pattern)
        expected = []

        self.assertEqual(results, expected)

    def test_empty_string(self):
        matcher = NaiveMatcher()

        text = "abc"
        pattern = ""

        results = matcher.match(text, pattern)
        expected = []

        self.assertEqual(results, expected)
