from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    unique_industries = set(
        [industry["industry"] for industry in file if industry["industry"]]
    )

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    job_filtered = [job for job in jobs if job["industry"] == industry]
    return job_filtered
