import random

from chromosome import Chromosome


map_file = './map.txt'
init_size = 200
mutate_probability = 0.3
minimum_average_difference = 0.2


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
    all_generations = []

    # Phase 1: Generate init population
    init_generation, avg = random_init(len(map_object))

    current_generation = init_generation
    prev_avg = 0
    curr_avg = avg

    while curr_avg - prev_avg > minimum_average_difference:

        # Phase 2, 3: selection
        selected = select(current_generation)
        all_generations.append(selected)                # Keeping all generations
        random.shuffle(selected)

        # Phase 4: Create next generation
        next_generation = []
        for i in range(0, init_size, 2):
            children = selected[i].create_children(selected[i+1])
            next_generation.extend(children)

        # Phase 5: Mutate
        for i in next_generation:
            if random.random() <= mutate_probability:
                i.mutate()

        prev_avg = curr_avg
        curr_avg = get_average(next_generation)
        current_generation = next_generation
        print(prev_avg, curr_avg)


main()
