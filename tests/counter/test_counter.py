from src.pre_built.counter import count_ocurrences


def test_counter():
    correct_path = "data/jobs.csv"
    word1_lc = "javascript"
    word1_uc = "JAVASCRIPT"
    word1_mixed = "JavaScript"
    count_word1 = 122

    assert count_ocurrences(correct_path, word1_lc) == count_word1
    assert count_ocurrences(correct_path, word1_uc) == count_word1
    assert count_ocurrences(correct_path, word1_mixed) == count_word1
    assert type(count_ocurrences(correct_path, word1_mixed)) is int
