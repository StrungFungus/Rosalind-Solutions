import unittest

def point_mutation_counter(seq1, seq2):
    differences = sum(1 for str1, str2 in zip(seq1, seq2) if str1 != str2)
    return differences


a = input("Input first strand:")
b = input("Input second strand:")
print(point_mutation_counter(a, b))

# class TestMutationCounter(unittest.TestCase):
#
#     def test_sample_case(self):
#         self.assertEqual(point_mutation_counter("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)
#
# if __name__ == '__main__':
#     unittest.main()
