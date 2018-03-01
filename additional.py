

def ride_is_optimal(vehicle, ride):
    if vehicle[4] == ride[4]:
        return True

def write_output(vehicles):
    submission = open('output.txt', 'w')
    for vehicle in vehicles:
        dim = len(vehicle[-1])
        submission.write("%d " % dim)
        for i in range(dim):
            submission.write("%d " % vehicle[-1][i])
        submission.write("\n")

vehicles = [0, 0, 0, [1, 2, 3]], [0, 0, 0, [4, 5]]
write_output(vehicles)
