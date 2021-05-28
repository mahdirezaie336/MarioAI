class Chromosome:

    __map = ''

    def __init__(self, string):
        self.string = string

    def __gt__(self, other):
        if not isinstance(other, Chromosome):
            raise ValueError('Operand is not type of Chromosome.')
        return self.calculate_fitness() > other.calculate_fitness()

    def __lt__(self, other):
        if not isinstance(other, Chromosome):
            raise ValueError('Operand is not type of Chromosome.')
        return self.calculate_fitness() < other.calculate_fitness()

    def __ge__(self, other):
        if not isinstance(other, Chromosome):
            raise TypeError('Operand is not type of Chromosome.')
        return self.calculate_fitness() >= other.calculate_fitness()

    def __le__(self, other):
        if not isinstance(other, Chromosome):
            raise ValueError('Operand is not type of Chromosome.')
        return self.calculate_fitness() <= other.calculate_fitness()

    def __str__(self):
        return '{}   {}   {}'.format(self.string, Chromosome.__map, self.calculate_fitness())

    def calculate_fitness(self):

        chromosome = self.string
        map_object = Chromosome.__map
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
            if j != len(map_object) - 1:  # if we are not on the last block

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

        return largest_path + extra_fitness

    @staticmethod
    def set_map(map_object: str):
        Chromosome.__map = map_object
