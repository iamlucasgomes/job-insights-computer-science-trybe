from src.pre_built.counter import count_ocurrences


def test_counter():
    count_ocurrences_python = count_ocurrences("data/jobs.csv", "Python")
    count_ocurrences_javascript = count_ocurrences(
        "data/jobs.csv", "Javascript"
    )

    assert count_ocurrences_python == 1639
    assert count_ocurrences_javascript == 122
