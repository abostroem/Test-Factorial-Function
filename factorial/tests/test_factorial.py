# import the function to test and some nosetools tools
from factorial.factorial import factorial
from nose.tools import assert_equal, assert_raises

# Here we define several good pairs of inputs and outputs to test
good_input_output_pairs = {
  0: 1,
  1: 1,
  10: 3628800,
}

# Now we run the tests to make sure the good inputs are followed by good outputs
def test_factorial_good_values():
    for arg, val in good_input_output_pairs.items():
        yield assert_equal, factorial(arg), val

# Define some inputs that should be caught as bad by the function
bad_inputs = [1.5, -10, -1.5, None, test_factorial_good_values, 'pants', '3']

# Now run the tests to make sure the bad inputs are caught
def test_factorial_for_bad_input():
    for bad in bad_inputs:
        yield assert_raises, AssertionError, factorial, bad
