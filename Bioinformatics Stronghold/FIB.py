import unittest

def rabbits(n, k):
    if n == 0:
        return 0
    rabbits = [1, 1]
    for i in range(2, n):
        rabbits.append(rabbits[i-1] + k * rabbits[i-2])
    print(rabbits[n - 1])
    return rabbits[n-1]


# n = int(input("Input N:"))
# k = int(input("Input k:"))
# rabbits(n, k)


class TestRabbitsFunction(unittest.TestCase):

    def test_sample_case(self):
        self.assertEqual(rabbits(5, 3), 19)

    def test_base_case_1(self):
        self.assertEqual(rabbits(1, 3), 1)

    def test_base_case_2(self):
        self.assertEqual(rabbits(2, 3), 1)

    def test_large_k(self):
        self.assertEqual(rabbits(4, 5), 11)

    def test_zero_months(self):
        self.assertEqual(rabbits(0, 3), 0)

if __name__ == '__main__':
    unittest.main()