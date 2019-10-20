from math import floor
from random import randint, randrange
import timeit
import matplotlib.pyplot as plt

from TwoSum0 import twosum as twosum0
from TwoSum1 import twosum as twosum1
from TwoSum2 import twosum as twosum2


class Test(object):
    def __init__(self, input_size, target=9):
        self.target = target
        self.input_size = input_size
        # Create list with numbers from 0 to halfway point so no soln exists yet.
        self.halfway = floor(self.target/2)
        self.input_array = [randint(0, self.halfway) for _ in range(self.input_size)]

    def run_test(self, alg):
        # Pick a number at random to replace with a number above midway
        # (only allow one solution in each test input)
        random_index = randrange(0, self.input_size)
        self.input_array[random_index] = randint(self.halfway+1, self.target)
        # only difference b/w range and int in this case is the inclusion of the
        # second input in possible outputs. [,) vs. [,]

        start = timeit.default_timer()
        if alg == 0:
            index_list = twosum0(self.input_array, self.target)
        elif alg == 1:
            index_list = twosum1(self.input_array, self.target)
        elif alg == 2:
            index_list = twosum2(self.input_array, self.target)
        else:
            print("Invalid algorithm specified")
            return

        stop = timeit.default_timer()

        if self.input_array[index_list[0]] + self.input_array[index_list[1]] != self.target:
            print("Error: result not equal to target.")
            return

        # revert input array to have no solution
        self.input_array[random_index] = randint(0, self.halfway)

        return stop-start

def runtime_calc(input_size, trials, alg):
    mytest = Test(input_size)

    runtimes = []
    for n in range(trials):
        runtimes.append(mytest.run_test(alg))

    avg_runtime = sum(runtimes)/len(runtimes)
    return avg_runtime


def runtime_plot(trials):
    input_sizes = [100, 500, 1000, 10000, 100000, 1000000]

    runtime_results = [[], [], []]
    for alg in [0, 1, 2]:
        for size in input_sizes:
            runtime_results[alg].append(runtime_calc(size, trials, alg))

    plt.plot(input_sizes, runtime_results[0], label='basic (range)')
    plt.plot(input_sizes, runtime_results[1], label='enumerate')
    plt.plot(input_sizes, runtime_results[2], label='hash table')

    plt.xlabel('Input Size')
    plt.ylabel('Avg Runtime (s)')
    plt.title("Runtime vs. Input Size")
    plt.legend()

    plt.show()









#
