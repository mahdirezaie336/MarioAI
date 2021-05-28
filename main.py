import random


map_file = './map.txt'
init_size = 200


def read_map(address: str) -> str:
    data = ''
    with open(address, 'r') as file:
        data += file.readline()
    return data


def random_init(chrom_length: int):
    res = []
    for i in range(init_size):
        chromosome = []
        for j in range(chrom_length):
            chromosome.append(str(random.randint(0, 2)))
        res.append(''.join(chromosome))
    return res


def main():
    map_object = read_map(map_file)
    init_generation = random_init(len(map_object))
    for i in init_generation:
        print(i)

main()
