from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    dictionary = []
    with open(path) as file:
        list = csv.DictReader(file)
        for line in list:
            dictionary.append(line)
    return dictionary


def get_unique_job_types(path: str) -> List[str]:
    file = read(path)
    unique_job_types = set()

    for job in file:
        unique_job_types.add(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
