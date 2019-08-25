"""Improved by moving input array to separate object to avoid rebuilding whole
array on every trial. Just modify array as much as necessary to provide different
solution."""

from math import floor
from random import randint, randrange
import timeit
import matplotlib.pyplot as plt

from TwoSum0 import twosum as twosum0
from TwoSum1 import twosum as twosum1
from TwoSum3 import twosum as twosum2


class InputArray(object):
    def __init__(self, size, target=9):
        self.array_size = size
        self.target = target

        # Create list with numbers from 0 to halfway point so no soln exists yet.
        self.halfway = floor(self.target / 2)
        self.array = [randint(0, self.halfway) for _ in range(self.array_size)]

        # initialize pointer for element that will contain the complement (solution)
        self.soln_index = 0

    def get_nosoln_array(self):
        # returns array with no solution

        # Since it is possible that the get_soln_array has mutated self.array
        # to include a solution, we must change the number at the solution index
        # back to a non-complementary value.
        self.array[self.soln_index] = randint(0, self.halfway)

        return self.array

    def get_soln_array(self):
        # Each time this method is called, a different solution will exist in the
        # returned array

        # Pick a number at random to replace with a number above midway
        # (only allow one solution in each test input)
        self.soln_index = randrange(0, self.array_size)
        self.array[self.soln_index] = randint(self.halfway+1, self.target)
        # only difference b/w range and int in this case is the inclusion of the
        # second input in possible outputs. [,) vs. [,]

        return self.array
        # this leaves the array mutated to include a solution.


class Test(object):
    def __init__(self, input_array, target=9):
        # input_array is an instance of the InputArray class
        self.array_obj = input_array
        self.target = target

    def run_test(self, alg):
        # every time this test object's run_test() method is used, the array is
        # the same as last time except the solution is changed.
        # using get_array() here produces the array with a unique solution every time it's called.
        self.input_array = self.array_obj.get_soln_array()

        if alg == 0:
            start = timeit.default_timer()
            index_list = twosum0(self.input_array, self.target)
        elif alg == 1:
            start = timeit.default_timer()
            index_list = twosum1(self.input_array, self.target)
        elif alg == 2:
            start = timeit.default_timer()
            index_list = twosum2(self.input_array, self.target)
        else:
            print("Invalid algorithm specified")
            return

        stop = timeit.default_timer()

        if self.input_array[index_list[0]] + self.input_array[index_list[1]] != self.target:
            print("Error: result not equal to target.")
            return

        return stop-start

def runtime_calc(input_size, trials, alg):
    myarray = InputArray(input_size)
    mytest = Test(myarray)

    runtimes = []
    for n in range(trials):
        runtimes.append(mytest.run_test(alg))

    avg_runtime = sum(runtimes)/len(runtimes)
    return avg_runtime


def runtime_plot(trials):
    input_sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

    runtime_results = [[], [], []]
    for alg in [2, 1, 0]:
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
