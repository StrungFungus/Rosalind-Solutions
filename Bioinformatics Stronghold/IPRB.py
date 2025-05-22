import unittest


def dominant_probability(k, m, n):
    T = k + m + n
    p = 1 - ((n * (n-1) + m * n + (1/4) * m * (m-1)) / (T * (T-1)))
    return p


# a = float(input("Input homozygous dominant population size:"))
# b = float(input("Input heterozygous population size:"))
# c = float(input("Input homozygous recessive population size:"))
# print(dominant_probability(a, b, c))


class TestDominantProbability(unittest.TestCase):

    def test_sample_case(self):
        self.assertEqual(dominant_probability(2, 2, 2), 0.78333)

if __name__ == '__main__':
    unittest.main()