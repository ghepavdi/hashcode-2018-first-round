"""
Hashcode 2018 first round

#test commit claudio
#test commit cristiano

"""

import sys
import numpy as np


def parse_input_file(filename):
    f = open("input/" + filename)

    line = f.readline()
    con = line.split(' ')
    r = int(con[0])
    c = int(con[1])

    min_t = int(con[2])  # minimum number of tomatoes and blabla
    max_size = int(con[3])  # max slice size

    matrix = np.zeros(shape=(r, c))
    m_i = 0
    for line in f:
        if not line.startswith(str(r)):
            indices = [i for i, ltr in enumerate(line) if ltr == 'T']
            matrix[m_i][indices] = 1
            m_i += 1
    f.close()
    return matrix, min_t, max_size


def write_output(filename, things_to_score):
    with open(filename[:-3] + ".out", "w") as file:
        file.write("{}\n".format())
        # for s in things_to_score:
        #     file.write("{} {} {} {}\n".format(s[0], s[1], s[2], s[3]))


def calculate_score(score_input):
    score = 0
    return score


FILENAME = sys.argv[1]
parse_input_file(FILENAME)
write_output(FILENAME, "")
