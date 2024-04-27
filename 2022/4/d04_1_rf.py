import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        raw_data = f.read()
        result = []
        for row in raw_data.split("\n"):
            if row.strip() == "":
                break
            (a, b), (c, d) = (x.split("-") for x in row.split(","))
            result.append(tuple(map(int, (a, b, c, d))))
        return result


def count_score(sections):
    score = 0
    for a, b, c, d in sections:
        is_first_bigger = a <= c and b >= d
        is_second_bigger = c <= a and d >= b
        if is_first_bigger or is_second_bigger:
            score += 1
    return score


if __name__ == "__main__":
    file_name = "input.txt"
    sections = read_data(file_name)
    score = count_score(sections)
    print(score)
