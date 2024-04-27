import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        game = f.read()
        result = []
        for round in game.split("\n"):
            if round.strip() == "":
                break
            pair = round.strip().split(" ")
            result.append(pair)
        return result


def count_game(game):
    balance = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }
    figure = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for elf, player in game:
        score += figure[player] + balance[(elf, player)]
    return score


if __name__ == "__main__":
    file_name = "input.txt"
    game = read_data(file_name)
    result = count_game(game)
    print(result)
