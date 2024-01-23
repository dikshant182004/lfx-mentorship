import unittest
from answer import process_list

# for robust testing

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = process_list(input_list)
        self.assertEqual(result, [1, 5, 7, 11, 13, 17, 19])

    def test_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with self.assertRaises(Exception) as context:
            process_list(input_list)
        self.assertEqual(str(context.exception), 'length is not a multiple of 10')

    def test_empty_input(self):
        input_list = []
        result = process_list(input_list)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        input_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        result = process_list(input_list)
        self.assertEqual(result, [-1, -5, -7])


if __name__ == '__main__':
    unittest.main()
