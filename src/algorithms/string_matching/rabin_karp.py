from typing import List

Prime = int


class RabinKarpMatcher:
    def match(self, text: str, pattern: str, d: int, q: Prime) -> List[int]:
        matches = []

        if text is None or pattern is None:
            return matches

        n, m = len(text), len(pattern)

        text_int = self._text_to_int(text)
        pattern_int = self._text_to_int(pattern)

        h = d ** (m - 1) % q
        t, p = 0, 0

        for pat, tex in zip(pattern_int, text_int):
            p = (d * p + pat) % q
            t = (d * t + tex) % q

        for s in range(n - m + 1):
            if p == t or pattern == "":
                if text[s : s + m] == pattern:
                    matches.append(s)

            if s < n - m:
                t = (d * (t - text_int[s] * h) + text_int[s + m]) % q

        return matches

    def _text_to_int(self, text: str) -> List[int]:
        return [ord(t) for t in text]
