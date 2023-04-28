from src.pre_built.sorting import sort_by


salary_list = [
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2023-05-01"},
    {"min_salary": 4500, "max_salary": 7500, "date_posted": "2023-05-03"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2023-05-02"},
]

min_salary = [
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2023-05-01"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2023-05-02"},
    {"min_salary": 4500, "max_salary": 7500, "date_posted": "2023-05-03"},
]

max_salary = [
    {"min_salary": 4500, "max_salary": 7500, "date_posted": "2023-05-03"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2023-05-02"},
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2023-05-01"},
]

date_posted = [
    {"min_salary": 4500, "max_salary": 7500, "date_posted": "2023-05-03"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2023-05-02"},
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2023-05-01"},
]


def test_sort_by_criteria():
    sort_by(salary_list, "min_salary")
    assert salary_list == min_salary
    sort_by(salary_list, "max_salary")
    assert salary_list == max_salary
    sort_by(salary_list, "date_posted")
    assert salary_list == date_posted
