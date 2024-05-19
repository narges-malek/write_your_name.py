import write_your_name as name_point

def test_hi_my_name_is():
    """
    Test the hi_my_name_is function from the write_your_name module.

    This function calls hi_my_name_is from the write_your_name module and 
    verifies that the returned string is non-empty and has a length greater than 1.
    """
    result = wyn.hi_my_name_is()
    print("Function output:", result)
    assert len(name_point.hi_my_name_is())  > 1 

test_hi_my_name_is()
