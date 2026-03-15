import unittest
from l1 import MatrixProcessor

class TestMatrixProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = MatrixProcessor()

    def test_add_matrices_success(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        result = self.processor.add_matrices(a, b)
        self.assertEqual(result, expected)

    def test_add_matrices_mismatch_size(self):
        a = [[1, 2], [3, 4]]
        b = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(ValueError) as context:
            self.processor.add_matrices(a, b)
        self.assertIn("однакові розміри", str(context.exception))

    def test_calculate_special_column_sum_basic(self):
        matrix = [
            [10, 20],
            [30, 5]
        ]
        result = self.processor.calculate_special_column_sum(matrix)
        self.assertEqual(result, 35)

    def test_calculate_special_column_sum_single_element(self):
        matrix = [[42]]
        # Стовпець 0 (парний): max([42]) = 42
        result = self.processor.calculate_special_column_sum(matrix)
        self.assertEqual(result, 42)

    def test_calculate_special_column_sum_empty(self):
        with self.assertRaises(ValueError):
            self.processor.calculate_special_column_sum([])
        with self.assertRaises(ValueError):
            self.processor.calculate_special_column_sum([[]])

    def test_calculate_special_column_sum_three_columns(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        result = self.processor.calculate_special_column_sum(matrix)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()