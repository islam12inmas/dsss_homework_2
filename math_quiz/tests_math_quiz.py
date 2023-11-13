import unittest
from math_quiz import random_integer, random_operator, formula_builder


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        rand_operator = random_operator()
        self.assertIn ['+', '-', '*']

    def test_build_formula(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (5, 3, '-', '5 - 3', 2), (9, 3, '+' , '9 + 3', 12), (4, 4,'*', '4 * 4', 16),
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = formula_builder(num1= num1, num2= num2, operator= operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
            
                
                

if __name__ == "__main__":
    unittest.main()
