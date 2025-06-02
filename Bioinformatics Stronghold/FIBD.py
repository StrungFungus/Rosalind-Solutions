import unittest

def rabbits(n, m):
    if n == 0:
        return 0
    ages = [1] + [0] * (m-1)
    for month in range(1,n):
        new = sum(ages[1:])
        ages = [new] + ages[:-1]
    return sum(ages)



# n = int(input("Input N:"))
# k = int(input("Input M:"))
# final = rabbits(n, k)
# print(final)



class TestRabbitsFunction(unittest.TestCase):

    def test_sample_case(self):
        self.assertEqual(rabbits(6, 3), 4)

    def test_base_case_1(self):
        self.assertEqual(rabbits(93, 17), 12081658148171622250)

    def test_base_case_2(self):
        self.assertEqual(rabbits(83, 16), 97817789207983710)

if __name__ == '__main__':
    unittest.main()