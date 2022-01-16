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

    def test_none_string_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "01010101001"
        pattern = None
        d = 2
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

    def test_empty_string_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "010"
        pattern = ""
        d = 2
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

    def test_single_match_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "01010"
        pattern = "1010"
        d = 2
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

    def test_double_match_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "01010"
        pattern = "10"
        d = 2
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

    def test_same_character_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "0000"
        pattern = "0"
        d = 2
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

    def test_bigger_pattern_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "0000"
        pattern = "010111010"
        d = 2
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

    def test_prefix_match_different_radix(self):
        matcher = RabinKarpMatcher()

        text = "0101020"
        pattern = "01020"
        d = 3
        q = 131

        results = matcher.match(text, pattern, d, q)
        expected = [2]

        self.assertEqual(results, expected)
