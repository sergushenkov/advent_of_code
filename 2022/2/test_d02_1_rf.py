from d02_1_rf import read_data, count_game


def test_read_data():
    game = read_data("test_input.txt")
    assert game == [["A", "Y"], ["B", "X"], ["C", "Z"]]


def test_count_game():
    game = [["A", "Y"], ["B", "X"], ["C", "Z"]]
    assert count_game(game) == 15
