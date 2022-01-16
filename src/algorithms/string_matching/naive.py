class NaiveMatcher:
    def match(text, pattern):
        n, m = len(text), len(pattern)
        matches = []

        for i in range(n - m):
            if text[i: i + m + 1] == pattern:
                matches.append(i)

        return matches
