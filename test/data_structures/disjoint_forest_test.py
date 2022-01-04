from src.data_structures.disjoint_forest import DisjointForest
import unittest


class TestDisjointForest(unittest.TestCase):
    def test_new_sets_are_disjoint(self):
        values = list(range(10))

        forest = DisjointForest()
        sets = [forest.make_set(v) for v in values]

        for s1, s2 in zip(sets, sets[1:]):
            self.assertFalse(forest.are_in_same_set(s1, s2))

    def test_joined_sets_arent_disjoint(self):
        forest = DisjointForest()
        s1, s2 = forest.make_set(), forest.make_set()

        self.assertFalse(forest.are_in_same_set(s1, s2))

        forest.join_sets(s1, s2)

        self.assertTrue(forest.are_in_same_set(s1, s2))

    def test_only_joined_sets_are_disjoint(self):
        values = list(range(10))

        forest = DisjointForest()
        sets = [forest.make_set(v) for v in values]

        for i in range(0, len(sets), 2):
            forest.join_sets(sets[i], sets[i + 1])

            for j in range(len(sets)):
                same_set = forest.are_in_same_set(sets[i], sets[j])

                if j == i or j == i + 1:
                    self.assertTrue(same_set)
                else:
                    self.assertFalse(same_set)

    def test_can_join_everything(self):
        values = list(range(20))

        forest = DisjointForest()
        sets = [forest.make_set(v) for v in values]

        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                self.assertFalse(forest.are_in_same_set(sets[0], sets[j]))

            forest.join_sets(sets[0], sets[i])

        for i in range(len(sets)):
            for j in range(len(sets)):
                self.assertTrue(forest.are_in_same_set(sets[i], sets[j]))
