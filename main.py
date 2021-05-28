import random

map_file = './map.txt'
init_size = 200
map_object = ''


def read_map(address: str) -> str:
    data = ''
    with open(address, 'r') as file:
        data += file.readline()
    return data


def random_init(chromosome_length: int):
    res = []
    for i in range(init_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(str(random.randint(0, 2)))
        res.append(''.join(chromosome))
    return res


def calculate_fitness(chromosome: str):

    extra_fitness = 0
    largest_path = 0
    path_length = 0
    is_on_air = False

    for j, item in enumerate(map_object):

        decision = chromosome[j]

        # Jumping twice which is undefined. We define it here
        if j != 0:
            if is_on_air and chromosome[j - 1] == '1':
                decision = '0'

        path_length += 1
        if j != len(map_object) - 1:                                    # if we are not on the last block

            next_decision = chromosome[j + 1]
            next_item = map_object[j + 1]

            # If we lose
            if ((not is_on_air) and next_item == 'G' and decision != '1') or (next_item == 'L' and decision != '2'):
                if path_length > largest_path:
                    largest_path = path_length
                path_length = 0
                continue

            # If we do unnecessary jump
            if next_item == '_' and decision != '0':
                extra_fitness += -0.5

            # If we eat mushroom
            if next_item == 'M' and decision != '1':
                extra_fitness += 2

            # If we kill a Goomba
            if j != len(chromosome) - 2 and map_object[j + 2] == 'G' and decision == '1':
                extra_fitness += 2

        else:
            # If we jump on flag
            if decision == '1':
                extra_fitness += 2

        is_on_air = decision == '1'

    # If we win
    if largest_path == 0:
        largest_path = 15

    return largest_path, extra_fitness


def main():
    global map_object
    map_object = read_map(map_file)
    init_generation = random_init(len(map_object))
    print(map_object)
    for i in init_generation:
        print(i, calculate_fitness(i), '\t\t',map_object)


main()
