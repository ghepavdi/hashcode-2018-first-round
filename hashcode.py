"""
Hashcode 2018 first round

# ottimizzazione: le rides che hanno inizio e fine in comune, assegnarle allo stesso veicoli
"""

import sys
import numpy as np


def parse_input_file(filename):
    f = open(filename)

    line = f.readline()
    con = line.split(' ')
    rows = int(con[0])
    cols = int(con[1])
    n_vehicles = int(con[2])
    n_rides = int(con[3])
    starting_bonus = int(con[4])
    n_steps = int(con[5])

    f.close()
    return rows, cols, n_vehicles, n_rides, starting_bonus, n_steps

def build_matrix(rows, cols):
    # TODO
    # matrix = np.zeros(shape=(r, c))
    # m_i = 0
    # for line in f:
    #     if not line.startswith(str(r)):
    #         indices = [i for i, ltr in enumerate(line) if ltr == 'T']
    #         matrix[m_i][indices] = 1
    #         m_i += 1
    return np.zeros((rows, cols))

def write_output(filename, things_to_score):
    with open(filename[:-3] + ".out", "w") as file:
        file.write("{}\n".format())
        # for s in things_to_score:
        #     file.write("{} {} {} {}\n".format(s[0], s[1], s[2], s[3]))


def calculate_score(score_input):
    score = 0
    return score


filename = sys.argv[1]
rows, cols, n_vehicles, n_rides, starting_bonus, n_steps = parse_input_file(filename)
print(rows, cols, n_vehicles, n_rides, starting_bonus, n_steps)
# write_output(FILENAME, "")
