class MatrixProcessor:
    """Клас для виконання операцій з матрицями згідно з варіантом."""

    def execute(self):
        """Головний метод, що виконує всі дії та обробляє виключення."""
        try:
            # Визначення значень у виконавчому методі
            # Тип int (згідно з C7=3)
            matrix_a = [
                [10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]
            ]

            matrix_b = [
                [5, 15, 25],
                [35, 45, 55],
                [65, 75, 85]
            ]

            print("--- Дія 1: Додавання матриць (C = A + B) ---")
            matrix_c = self.add_matrices(matrix_a, matrix_b)
            self.print_matrix(matrix_c)

            print("\n--- Дія 2: Розрахунок специфічної суми стовпців (C11=6) ---")
            result_sum = self.calculate_special_column_sum(matrix_c)
            print(f"Результат суми: {result_sum}")

        except ValueError as e:
            print(f"Помилка у значеннях або розмірності: {e}")
        except TypeError as e:
            print(f"Помилка типу даних: {e}")
        except Exception as e:
            print(f"Виникла непередбачена помилка: {e}")

    def add_matrices(self, a, b):
        """Виконує додавання двох матриць."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Матриці повинні мати однакові розміри для додавання.")

        rows = len(a)
        cols = len(a[0])
        # Створення результуючої матриці через list comprehension
        result = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]
        return result

    def calculate_special_column_sum(self, matrix):
        """
        Обчислює суму найбільших елементів у парних стовпцях
        та найменших у непарних стовпцях.
        """
        if not matrix or not matrix[0]:
            raise ValueError("Матриця порожня.")

        rows = len(matrix)
        cols = len(matrix[0])
        total_sum = 0

        for j in range(cols):
            # Отримуємо всі елементи поточного стовпця j
            column_elements = [matrix[i][j] for i in range(rows)]

            if j % 2 == 0:
                # Парний індекс стовпця (0, 2...) -> Шукаємо MAX
                current_val = max(column_elements)
                print(f"Стовпець {j} (парний): max = {current_val}")
            else:
                # Непарний індекс стовпця (1, 3...) -> Шукаємо MIN
                current_val = min(column_elements)
                print(f"Стовпець {j} (непарний): min = {current_val}")

            total_sum += current_val

        return total_sum

    def print_matrix(self, matrix):
        """Вивід матриці у зручному форматі."""
        for row in matrix:
            print("\t".join(map(str, row)))


if __name__ == "__main__":
    processor = MatrixProcessor()
    processor.execute()