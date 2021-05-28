import random
from chromosome import Chromosome


map_file = './map.txt'
init_size = 200


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
        c = Chromosome(''.join(chromosome))
        sum_ += c.get_fitness()
        res.append(c)
    return res, sum_/init_size


def main():
    map_object = read_map(map_file)
    Chromosome.set_map(map_object)
    init_generation, avg = random_init(len(map_object))

    for i in init_generation:
        print(i)
    print(avg)


main()
