import price_info as pi

def test_tcs():
    assert(pi.total_cost_shopping() == 46.75)
def test_cof():
    assert(pi.cost_of_fruits('orange',5) == 7)