import random
import matplotlib.pyplot as plt

from chromosome import Chromosome
from screen_manager import Display

map_file = './maps/level4.txt'
init_size = 500
mutate_probability = 0.3
min_difference = 0.0005
comb_length = 2
consider_winning_score = False


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
    return res, sum_ / init_size


def get_average(generation: list[Chromosome]) -> float:
    sum_ = 0
    for g in generation:
        sum_ += g.get_fitness()
    return sum_ / init_size


def select(generation: list[Chromosome]) -> list[Chromosome]:
    generation.sort()
    result = generation[init_size // 2:init_size]
    result.extend(generation[init_size // 2:init_size])
    return result


def main():
    map_object = read_map(map_file)
    Chromosome.set_map(map_object)
    Chromosome.set_winning_score(consider_winning_score)
    all_generations = []
    mins = []
    maxs = []
    averages = []

    # Phase 1: Generate init population
    init_generation, avg = random_init(len(map_object))

    current_generation = init_generation
    prev_avg = 0
    curr_avg = avg
    # averages.append(avg)

    while curr_avg - prev_avg > min_difference or curr_avg - prev_avg < -1 * min_difference:

        # Phase 2, 3: selection
        selected = select(current_generation)
        all_generations.append(current_generation)  # Keeping all generations
        maxs.append(current_generation[-1].get_fitness())
        mins.append(current_generation[0].get_fitness())
        random.shuffle(selected)

        # Phase 4: Create next generation
        next_generation = []
        for i in range(0, init_size, 2):
            length = random.randint(0, init_size - 1 - comb_length)
            a, b = length, length + comb_length
            children = selected[i].create_children(selected[i + 1], a, b)
            next_generation.extend(children)

        # Phase 5: Mutate
        for i in next_generation:
            if random.random() <= mutate_probability:
                i.mutate()

        prev_avg = curr_avg
        curr_avg = get_average(next_generation)
        current_generation = next_generation
        averages.append(curr_avg)
        print(prev_avg, curr_avg)

    print('Latest Solution:')
    print(all_generations[-1][-1])

    # Plotting
    indices = list(range(len(all_generations)))
    line_min, = plt.plot(indices, mins, 'm')
    line_max, = plt.plot(indices, maxs, 'y')
    line_avg, = plt.plot(indices, averages, 'c')
    plt.legend([line_min, line_max, line_avg], ['Minimum', 'Maximum', 'Average'])
    plt.show()

    # Display Game
    display = Display(map_object)
    display.begin_display()
    display.run_solution(all_generations[-1][-1].get_string())


main()
