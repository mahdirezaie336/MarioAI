import random
from chromosome import Chromosome


map_file = './map.txt'
init_size = 200
map_object = ''


def read_map(address: str) -> str:
    data = ''
    with open(address, 'r') as file:
        data += file.readline()
    return data


def random_init(chromosome_length: int) -> (list[Chromosome], int):
    res = []
    sum_ = 0
    for i in range(init_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(str(random.randint(0, 2)))
        Chromosome(''.join(chromosome))
        res.append()
    return res


def main():
    global map_object
    map_object = read_map(map_file)
    Chromosome.set_map(map_object)
    init_generation = random_init(len(map_object))

    for i in init_generation:
        print(i)


main()
