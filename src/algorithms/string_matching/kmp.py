from typing import List


class KnuthMorrisPrattMatcher:
    def match(self, text: str, pattern: str) -> List[int]:
        matches = []

        if text is None or pattern is None:
            return matches

        n, m = len(text), len(pattern)

        prefixes = self._compute_prefix_array(pattern)

        q = 0
        for i in range(1, n):
            while q > 0 and pattern[q] != pattern[i]:
                q = prefixes[q]

            if pattern[q] == pattern[i]:
                q += 1

            if q == m:
                matches.append(i)

                q = prefixes[q]

        return matches

    def _compute_prefix_array(self, pattern):
        m = len(pattern)

        prefixes = [0 for _ in range(m)]

        k = 0

        for q in range(1, m):
            while k > 0 and pattern[q] != pattern[k]:
                k = prefixes[k]

            if pattern[q] == pattern[k]:
                k += 1

            prefixes[q] = k

        return prefixes
