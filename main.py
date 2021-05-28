import random

from chromosome import Chromosome


map_file = './map.txt'
init_size = 200


def read_map(address: str) -> str:
    data = ''
    with open(address, 'r') as file:
        data += file.readline()
    return data


def random_init(chromosome_length: int) -> (list[Chromosome], float):
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


def get_average(generation: list[Chromosome]) -> float:
    sum_ = 0
    for g in generation:
        sum_ += g.get_fitness()
    return sum_/init_size


def select(generation: list[Chromosome]) -> list[Chromosome]:
    generation.sort()
    result = generation[init_size//2:init_size]
    result.extend(generation[init_size//2:init_size])
    return result


def main():
    map_object = read_map(map_file)
    Chromosome.set_map(map_object)

    # Phase 1: Generate init population
    init_generation, avg = random_init(len(map_object))

    # Phase 2: selection
    selected = select(init_generation)
    random.shuffle(selected)




main()
