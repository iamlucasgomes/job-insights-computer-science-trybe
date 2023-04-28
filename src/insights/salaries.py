from typing import Union, List, Dict
from .jobs import read
import sys


def get_max_salary(path: str) -> int:
    file = read(path)

    list_salary = [
        int(salary["max_salary"])
        for salary in file
        if salary["max_salary"].isdigit()
    ]
    return max(list_salary)


def get_min_salary(path: str) -> int:
    file = read(path)

    list_salary = [
        int(salary["min_salary"])
        for salary in file
        if salary["min_salary"].isdigit()
    ]
    return min(list_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        sal = int((salary))
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
    except (ValueError, TypeError, KeyError):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return min_salary <= sal <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    salary_within_expectations = []
    for job in jobs:
        try:
            salary_range = matches_salary_range(job, salary)
            if salary_range:
                salary_within_expectations.append(job)
        except ValueError:
            print(f"{job} contém um valor invalido", file=sys.stderr)
    return salary_within_expectations
