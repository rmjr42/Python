import unittest
from Grades import sum_grades, average_grades, grade_letter

class TestGrades(unittest.TestCase):

    def test_sum_grades(self):
        self.assertEqual(sum_grades([100, 90, 77, 66, 99]), 432)
        self.assertEqual(sum_grades([60, 70, 80, 90, 100]), 400)
        self.assertEqual(sum_grades([0, 0, 0, 0, 0]), 0)
        self.assertEqual(sum_grades([100, 100, 100, 100, 100]), 500)

    def test_average_grades(self):
        self.assertEqual(average_grades([100, 90, 77, 66, 99]), 86.4)
        self.assertEqual(average_grades([60, 70, 80, 90, 100]), 80)
        self.assertEqual(average_grades([0, 0, 0, 0, 0]), 0)
        self.assertEqual(average_grades([100, 100, 100, 100, 100]), 100)

    def test_grade_letter(self):
        self.assertEqual(grade_letter(95), 'A')
        self.assertEqual(grade_letter(85), 'B')
        self.assertEqual(grade_letter(75), 'C')
        self.assertEqual(grade_letter(65), 'D')
        self.assertEqual(grade_letter(55), 'F')

if __name__ == '__main__':
    unittest.main()