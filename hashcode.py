"""
Hashcode 2018 first round

# ottimizzazione: le rides che hanno inizio e fine in comune, assegnarle allo stesso veicoli
"""

import sys
import numpy as np


def get_ride_start(ride):
    return [ride[0], ride[1]]

def get_ride_end(ride):
    return [ride[2], ride[3]]

def get_ride_times(ride):
    return [ride[4], ride[5]]

def distance(start_point, end_point):
    a, b = start_point
    x, y = end_point
    return abs(a - x) + abs(b - y) 


def calculate_ride_score(rides,bonus,ride_id,current_step):
    score=0
    current_ride=rides[ride_id]#xstart, ystart, xfinish, yfinish, earliest_start, latest_finish
    x_start,y_start=get_ride_start(current_ride)
    x_finish, y_finish=get_ride_end(current_ride)
    earliest_start, latest_finish=get_ride_times(current_ride)
    """if finished_time> latest_finish:
        return 0# I finished too late, no score"""
    if current_step==earliest_start:
        score+=bonus#yay I started in time
    number_of_steps=abs(x_start-x_finish)+abs(y_start-y_finish)
    score+=number_of_steps
    return score


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
    rides = []

    for line in f:
        values = line.split(' ')
        rides.append(np.array([int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5]), 0]))

    np_rides = np.array(rides)

    f.close()
    return rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, np_rides

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



def create_vehicles(n_vehicles):
    # state_enum, x, y, id_ride
    vehicles = []
    for i in range(n_vehicles):
        vehicles.append(np.array([0, 0, 0, 0]))
    return np.array(vehicles)


filename = sys.argv[1]
rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, rides = parse_input_file(filename)
vehicles = create_vehicles(n_vehicles)
print("params: ", rows, cols, n_vehicles, n_rides, starting_bonus, n_steps)
print("rides: ", rides)
print("vehicles: ", vehicles)
# write_output(FILENAME, "")
