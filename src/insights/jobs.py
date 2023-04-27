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
    unique_job_types = set(
        [job["job_type"] for job in file if job["job_type"]]
    )

    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_filtered = [
        job for job in jobs if job["job_type"] == job_type
    ]
    return job_filtered
