from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    unique_industries = set(
        [industry["industry"] for industry in file if industry["industry"]]
    )

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
