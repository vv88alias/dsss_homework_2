import unittest
from math_quiz import random_number_generator, random_operator, calculation


class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random operators generated are within the specified range of operators
        operators = ['+', '-', '*']
        for i in range(1000):  # Test a large number of random values
            operat = random_operator()
            self.assertIn(operat, operators)

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 6, '-', '9 - 6', 3),
                (7, 2, '*', '7 * 2', 14)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
