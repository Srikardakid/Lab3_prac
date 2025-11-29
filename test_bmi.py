import bmi.py as bmi

def test_bmi_underweight():
    assert(bmi.calculate_bmi(1.90,45)) == -1
def test_bmi_normalweight():
    assert(bmi.calculate_bmi(1.77,61)) == 0
def test_bmi_overweight():
    assert(bmi.calculate_bmi(1.40,78)) == 1


