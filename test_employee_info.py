import employee_info as ei

def test_age():
    emp_list = [{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    assert(ei.get_employees_by_age_range(20,25) == emp_list)
def test_calc_avg():
    assert(ei.calculate_average_salary() == 180500/3)
def test_dept():
    emp_data = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(ei.get_employees_by_dept('Engineering') == emp_data)