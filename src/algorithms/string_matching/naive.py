from typing import List


class NaiveMatcher:
    def match(self, text: str, pattern: str) -> List[int]:
        matches = []

        if text is None or pattern is None:
            return matches

        n, m = len(text), len(pattern)

        for i in range(n - m):
            if text[i : i + m + 1] == pattern:
                matches.append(i)

        return matches
