"""
Hashcode 2018 first round

# ottimizzazione: le rides che hanno inizio e fine in comune, assegnarle allo stesso veicoli
"""

import sys
import numpy as np
from enum import Enum

class VehicleState(Enum):
    NO_RIDE = 0
    GOING_TO_RIDE = 1
    ON_RIDE = 2

def get_ride_start(ride):
    return [ride[0], ride[1]]

def get_ride_end(ride):
    return [ride[2], ride[3]]

def get_ride_times(ride):
    return [ride[4], ride[5]]

def get_ride_time_to_complete(ride):
    return distance(get_ride_start(ride), get_ride_end(ride))

def get_vehicle_state(vehicle):
    return vehicle[0]

def get_vehicle_position(vehicle):
    return [vehicle[1], vehicle[2]]

def get_vehicle_ride(vehicle):
    state = get_vehicle_state(vehicle)
    if state == VehicleState.GOING_TO_RIDE or state == VehicleState.ON_RIDE:
        return vehicle[3]

def distance(start_point, end_point):
    a, b = start_point
    x, y = end_point
    return abs(a - x) + abs(b - y) 

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

def ride_can_be_made(ride, current_step, max_step):
    time_to_complete_ride = get_ride_time_to_complete(ride)
    # NOTE: <= ???
    return (current_step + time_to_complete_ride) <= max_step

def ride_can_be_made_by_vehicle(vehicle, ride, current_step, max_step):
    vehicle_pos = get_vehicle_position(vehicle)
    ride_start_pos = get_ride_start(ride)
    time_to_get_to_ride = distance(vehicle_pos, ride_start_pos)
    time_to_complete_ride = get_ride_time_to_complete(ride)
    return (current_step + time_to_get_to_ride + time_to_complete_ride) <= max_step

filename = sys.argv[1]
rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, rides = parse_input_file(filename)
print(rows, cols, n_vehicles, n_rides, starting_bonus, n_steps)
print(rides)
# write_output(FILENAME, "")
