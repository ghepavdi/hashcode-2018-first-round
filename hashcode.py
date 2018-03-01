"""
Hashcode 2018 first round

# ottimizzazione: le rides che hanno inizio e fine in comune, assegnarle allo stesso veicoli
"""

import sys
# import numpy as np
from enum import Enum
import random


class VehicleState(Enum):
    NO_RIDE = 0
    GOING_TO_RIDE = 1
    ON_RIDE = 2

class RideState(Enum):
    ASSIGNED = 0
    UNASSIGNED = 1
    COMPLETED = 2

def get_ride_start(ride):
    return [ride[0], ride[1]]


def get_ride_end(ride):
    return [ride[2], ride[3]]


def get_ride_times(ride):
    return [ride[4], ride[5]]


def get_ride_time_to_complete(ride):
    return distance(get_ride_start(ride), get_ride_end(ride))

def is_ride_completed(ride):
    return ride[-1] is RideState.COMPLETED

def is_ride_assigned(ride):
    return ride[-1] is RideState.ASSIGNED

def set_ride_completed(ride):
    ride[-1] = RideState.COMPLETED

def set_ride_state(ride, state):
    ride[-1] = state

def get_vehicle_state(vehicle):
    return vehicle[0]

def set_vehicle_state(vehicle, state):
    vehicle[0] = state

def get_vehicle_position(vehicle):
    return [vehicle[1], vehicle[2]]

def set_vehicle_position(vehicle, pos):
    vehicle[1] = pos[0]
    vehicle[2] = pos[1]

def get_vehicle_ride(vehicle, rides):
    if len(vehicle[4]) > 0:
        return rides[vehicle[4][-1]]
    else:
        return None

def set_vehicle_ride(vehicle, ride_index):
    vehicle[-1].append(ride_index)

def get_vehicle_remaining_turns(vehicle):
    return vehicle[3]

def set_vehicle_remaining_turns(vehicle, n):
    vehicle[3] = n

def distance(start_point, end_point):
    a, b = start_point
    x, y = end_point
    return abs(a - x) + abs(b - y)


def calculate_ride_score_greedy(rides, bonus, ride_id, current_step,current_x,current_y):
    score = 0
    current_ride = rides[ride_id]  # xstart, ystart, xfinish, yfinish, earliest_start, latest_finish
    x_start, y_start = get_ride_start(current_ride)
    x_finish, y_finish = get_ride_end(current_ride)
    earliest_start, latest_finish = get_ride_times(current_ride)

    number_of_steps = distance((x_start,y_start),(x_finish,y_finish))
    score += number_of_steps

    timeToArrive=distance((current_x,current_y),(x_start,y_start))
    if current_step+timeToArrive==earliest_start:
        score+=bonus
    timeToWait=earliest_start-current_step+timeToArrive

    score=score - timeToArrive-timeToWait

    return score


def calculate_ride_score(rides,bonus,ride_id,current_turn):
    score=0
    current_ride = rides[ride_id]  # xstart, ystart, xfinish, yfinish, earliest_start, latest_finish
    x_start, y_start = get_ride_start(current_ride)
    x_finish, y_finish = get_ride_end(current_ride)
    earliest_start, latest_finish = get_ride_times(current_ride)

    if current_turn==earliest_start:
        print("wew")
        score+=bonus

    score+=distance((x_start,y_start),(x_finish,y_finish))

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
        rides.append(
            [int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5]), RideState.UNASSIGNED])

    f.close()
    return rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, rides


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


def create_vehicles(n_vehicles):
    # state_enum, x, y, remaining_turns, ride list
    vehicles = []
    for i in range(n_vehicles):
        vehicles.append([VehicleState.NO_RIDE, 0, 0, -1, []])
    return vehicles


def simulate(max_turns, vehicles, rides, bonus):
    """
    Scorriamo i veicoli e guardiamo se sono giunti a destinazione:
        modifichiamo lo stato del veicolo
            fermo, settiamo posizione di fine della ride appena finita
        settiamo la ride come completata

    Per ogni veicolo:
	    GOING_TO_RIDE
		    se non sei arrivato:
			    decrementare counter turni
		    altrimenti:
                controllare che il turno sia >= dello starting time
                    settare in GOING_TO_RIDE
        ON_RIDE
            decrementiamo il counter dei turni
        NO_RIDE
            prendo una ride che posso eseguire
		TODO: Gestire caso in cui la nuova ride ha coordinate di partenza coincidenti con la posizione attuale
    """
    ride_indexes = [i for i in range(len(rides))]
    random.shuffle(ride_indexes)
    print("Simulation start")
    score = 0
    for t in range(max_turns):
        for v in vehicles:
            v_state = get_vehicle_state(v)
            if v_state is VehicleState.GOING_TO_RIDE:
                if get_vehicle_remaining_turns(v) > 0:
                    set_vehicle_remaining_turns(v, get_vehicle_remaining_turns(v) - 1)
                else:
                    if t >= get_ride_times(get_vehicle_ride(v, rides))[0]:
                        set_vehicle_state(v, VehicleState.ON_RIDE)
            if v_state is VehicleState.ON_RIDE:
                set_vehicle_remaining_turns(v, get_vehicle_remaining_turns(v) - 1)
                if get_vehicle_remaining_turns(v) == 0:
                    set_vehicle_state(v, VehicleState.NO_RIDE)
                    curr_ride = get_vehicle_ride(v, rides)
                    set_vehicle_position(v, get_ride_end(curr_ride))
                    set_ride_completed(curr_ride)
            if v_state is VehicleState.NO_RIDE:
                for r in ride_indexes:
                    ride_start = get_ride_start(rides[r])
                    vehicle_pos = get_vehicle_position(v)
                    if ride_can_be_made_by_vehicle(v, rides[r], t, max_turns) and ride_start[0] == vehicle_pos[0] and ride_start[1] == vehicle_pos[1]:
                        set_vehicle_ride(v, r)
                        set_ride_state(rides[r], RideState.ASSIGNED)
                        ride_indexes.remove(r)
                        score += calculate_ride_score(rides, bonus, r, t)
                        break
                for r in ride_indexes:
                    if ride_can_be_made_by_vehicle(v, rides[r], t, max_turns):
                        set_vehicle_ride(v, r)
                        set_ride_state(rides[r], RideState.ASSIGNED)
                        ride_indexes.remove(r)
                        score += calculate_ride_score(rides, bonus, r, t)
                        break
    return score

def ride_is_optimal(vehicle, ride):
    if vehicle[4] == ride[4]:
        return True

def write_output(filename, vehicles):
    submission = open(filename + '_out.txt', 'w')
    for vehicle in vehicles:
        dim = len(vehicle[-1])
        submission.write("%d " % dim)
        for i in range(dim):
            submission.write("%d " % vehicle[-1][i])
        submission.write("\n")

filename = 'input/b_should_be_easy.in'
# filename.append('input/a_example.in')
# filename.append('input/b_should_be_easy.in')
# filename.append('input/c_no_hurry.in')
# filename.append('input/d_metropolis.in')
# filename.append('input/e_high_bonus.in')

# for file in filename:
# rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, rides = parse_input_file(filename)
# vehicles = create_vehicles(n_vehicles)

best_score = 0
while True:
    rows, cols, n_vehicles, n_rides, starting_bonus, n_steps, rides = parse_input_file(filename)
    vehicles = create_vehicles(n_vehicles)
    curr_score = simulate(n_steps, vehicles, rides, starting_bonus)
    print(curr_score)
    if curr_score > best_score:
        print("YAY", curr_score)
        write_output(filename, vehicles)
        best_score = curr_score

# print("params: ", rows, cols, n_vehicles, n_rides, starting_bonus, n_steps)
# print("rides: ", rides)
# print("vehicles: ", vehicles)

write_output(filename, vehicles)
