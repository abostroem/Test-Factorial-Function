def factorial(n):
    """
    Function that takes a nonzero integer and returns its factorial.  Its the
    main function in my repo used for our good coding and project practice
    meetings.
    """

    # First make sure the input is a number
    try:
        n+1
    except:
        raise AssertionError("n is not a number")

    # Then make sure it is a nonnegative integer
    assert isinstance(n, int), "not an integer"
    assert n>=0, 'int must be greater than 0'

    # Now execute the algorithm for finding the factorial
    # Return 1 for the case that the input is 0
    if n == 0:
        return 1

    # For positive input, loop over all integers up to the input, multiplying
    # the integers by a stored value, starting at 1.
    answer = 1
    for i in range(1,n+1):
        answer = i*answer

    # Return the answer for positive integer input
    return answer
