from y2023.day09.d09 import next_value, prev_value, answer, all_history


# def test_answer():
#     """ Тест для
#     def next_value(seq):
#         return seq[-1]"""
#     result = answer(all_history)
#     assert result == 81


def test_next_value():
    seq = [7, 7, 7]
    result = next_value(seq)
    assert result == 7

    seq = [0, 3, 6, 9, 12, 15]
    result = next_value(seq)
    assert result == 18
    seq = [1, 3, 6, 10, 15, 21]
    result = next_value(seq)
    assert result == 28
    seq = [10, 13, 16, 21, 30, 45]
    result = next_value(seq)
    assert result == 68


def test_prev_value():
    seq = [7, 7, 7]
    result = prev_value(seq)
    assert result == 7
    seq = [0, 3, 6, 9, 12, 15]
    result = prev_value(seq)
    assert result == -3
    seq = [1, 3, 6, 10, 15, 21]
    result = prev_value(seq)
    assert result == 0
    seq = [10, 13, 16, 21, 30, 45]
    result = prev_value(seq)
    assert result == 5