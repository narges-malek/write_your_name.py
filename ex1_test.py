import write_your_name as wyn

def test_hi_my_name_is():
    result = wyn.hi_my_name_is()
    print("Function output:", result)
    assert len(result)  > 1


test_hi_my_name_is()

