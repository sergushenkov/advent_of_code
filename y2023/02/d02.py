import os


def check_possible_games(games, bug):
    possible_games = []
    total_power = 0
    for game in games.splitlines():
        string_number, sets = game.split(": ")
        game_number = int(string_number[5:])
        max_color = {"red": 0, "green": 0, "blue": 0}
        for once_set in sets.split("; "):
            for color_number in once_set.split(", "):
                for color in max_color:
                    if color in color_number:
                        current_color_number = int(color_number[: -len(color)])
                        max_color[color] = max(current_color_number, max_color[color])
                        break
        is_possible_game = True
        power = 1
        for color, number in max_color.items():
            if number > bug[color]:
                is_possible_game = False
            power *= number
        if is_possible_game:
            possible_games.append(game_number)
        total_power += power
    return possible_games, total_power


test_games = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
bug = {"red": 12, "green": 13, "blue": 14}
assert check_possible_games(test_games, bug) == ([1, 2, 5], 2286)

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    possible_games, power = check_possible_games(fd.read(), bug)
    print(sum(possible_games), power)
