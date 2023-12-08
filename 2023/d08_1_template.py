import os


def find_variants(races):

    return variants


test_races = """"""
variants = find_variants(test_races)
assert variants == 71503


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    variants = find_variants(fd.read())
    print(variants)
