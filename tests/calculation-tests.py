import sys
sys.path.append('../')
from src.datacost import cost_labelling_positive, cost_labelling_negative
import unittest

class test_calculations(unittest.TestCase):

  # Initialize a cost matrix which can be used in testing.
  cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1, 'FN' : 5}

  def test_cost_labelling_positive(self):
    # Test that if <3 or >3 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      cost_labelling_positive(2, 3)
      cost_labelling_positive(2, 3, 7, self.cost_matrix)
    # Test a simple case with 2 positive and 3 negative data points.
    self.assertEqual(cost_labelling_positive(2, 3, self.cost_matrix), 5)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      cost_labelling_positive(2, 3, bad_cost_matrix)

  def test_cost_labelling_negative(self):
    # Test that if <3 or >3 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      cost_labelling_negative(2, 3)
      cost_labelling_negative(2, 3, 7, self.cost_matrix)
    # Test a simple case with 2 positive and 3 negative data points.
    self.assertEqual(cost_labelling_negative(2, 3, self.cost_matrix), 10)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      cost_labelling_negative(2, 3, bad_cost_matrix)

if __name__ == '__main__':
    unittest.main(exit=False)