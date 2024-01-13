from day09.test_d09_1 import next_value, answer, all_history


def test_answer():
    def next_value(seq):
        return seq[-1]

    result = answer(all_history)
    assert result == 81
