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

    for j, item in enumerate(map_object):

        decision = chromosome[j]

        # Jumping twice which is undefined. We define it here
        if j != 0:
            if decision == '1' and chromosome[j - 1] == '1':
                decision = '0'

        path_length += 1
        if j != len(map_object) - 1:                                    # if we are not on the last

            next_decision = chromosome[j + 1]
            next_item = map_object[j + 1]

            # If we lose
            if (next_item == 'G' and (decision == '0' or decision == '2')) or \
                    (next_item == 'L' and (decision == '0' or decision == '1')):
                if path_length > largest_path:
                    largest_path = path_length
                path_length = 0

            # If we do unnecessary jump
            if next_item == '_' and (decision == '1' or decision == '2'):
                extra_fitness += -0.5

            # If we eat mushroom
            if next_item == 'M' and decision == '0':
                extra_fitness += 2

            # If we kill a Goomba
            if j != len(chromosome) - 2 and map_object[j + 2] == 'G' and decision == '1' \
                    and (next_decision == '1' or next_decision == '0'):
                extra_fitness += 2

        else:
            # If we jump on flag
            if decision == '1':
                extra_fitness += 2



def main():
    global map_object
    map_object = read_map(map_file)
    init_generation = random_init(len(map_object))
    for i in init_generation:
        print(i)


main()
