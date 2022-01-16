from typing import List


class KnuthMorrisPrattMatcher:
    def match(self, text: str, pattern: str) -> List[int]:
        matches = []

        if text is None or pattern is None:
            return matches

        n, m = len(text), len(pattern)

        prefixes = self._compute_prefix_array(pattern)

        q = 0
        for i in range(0, n):
            while q > 0 and text[i] != pattern[q]:
                q = prefixes[q - 1]

            # q >= m iff pattern == ""
            if q < m and text[i] == pattern[q]:
                q += 1

            if q == m:
                match_index = i - m + 1 if m > 0 else i
                matches.append(match_index)

                q = prefixes[q - 1]

        return matches

    def _compute_prefix_array(self, pattern):
        m = len(pattern)

        prefixes = [0 for _ in range(m)] if pattern != "" else [0]

        k = 0

        for q in range(1, m):
            while k > 0 and pattern[q] != pattern[k]:
                k = prefixes[k]

            if pattern[q] == pattern[k]:
                k += 1

            prefixes[q] = k

        return prefixes
