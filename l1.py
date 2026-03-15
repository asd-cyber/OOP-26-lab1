import unittest
import sys


class MatrixProcessor:

    def execute(self):
        try:
            matrix_a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
            matrix_b = [[5, 15, 25], [35, 45, 55], [65, 75, 85]]

            print("\n" + "=" * 40)
            print("ДІЯ 1: ДОДАВАННЯ МАТРИЦЬ (C = A + B)")
            print("=" * 40)

            matrix_c = self.add_matrices(matrix_a, matrix_b)
            self.print_matrix(matrix_c)

            print("\n" + "=" * 40)
            print("ДІЯ 2: ПОШУК MAX/MIN У СТОВПЦЯХ (C11=6)")
            print("=" * 40)
            result_sum = self.calculate_special_column_sum(matrix_c)
            print(f"\nЗАГАЛЬНА СУМА: {result_sum}")

        except Exception as e:
            print(f"Помилка під час виконання: {e}")

    def add_matrices(self, a, b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Матриці повинні мати однакові розміри.")
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    def calculate_special_column_sum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        total_sum = 0
        for j in range(cols):
            column = [matrix[i][j] for i in range(rows)]
            if j % 2 == 0:
                val = max(column)
                print(f"Стовпець {j} (парний): max = {val}")
            else:
                val = min(column)
                print(f"Стовпець {j} (непарний): min = {val}")
            total_sum += val
        return total_sum

    def print_matrix(self, matrix):
        for row in matrix:
            print("\t".join(map(str, row)))


class TestMatrixProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = MatrixProcessor()

    def test_add_matrices(self):
        a = [[1, 1], [1, 1]]
        b = [[2, 2], [2, 2]]
        self.assertEqual(self.processor.add_matrices(a, b), [[3, 3], [3, 3]])

    def test_special_sum_logic(self):
        matrix = [[10, 20], [30, 5]]
        self.assertEqual(self.processor.calculate_special_column_sum(matrix), 35)


if __name__ == "__main__":
    p = MatrixProcessor()
    p.execute()
    print("\n" + "-" * 40)
    print("РЕЗУЛЬТАТИ ТЕСТУВАННЯ:")
    print("-" * 40)
    unittest.main(argv=[sys.argv[0]], exit=False, buffer=True)