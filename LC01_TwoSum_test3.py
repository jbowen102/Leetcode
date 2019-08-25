"""Restructured to reuse same data structure for different input sizes
Something's not working right though. Got mem error one time,
and crashed Linux another time."""

from math import floor
from random import randint, randrange
import timeit
import matplotlib.pyplot as plt

from TwoSum0 import twosum as twosum0
from TwoSum1 import twosum as twosum1
from TwoSum2 import twosum as twosum2


class BaseArray(object):
    def __init__(self, init_size=100, target=9):
        # Create list with numbers from 0 to halfway point so no soln exists yet.
        self.size = init_size
        self.halfway = floor(target / 2)
        self.array = [randint(0, self.halfway) for _ in range(self.size)]
    def get_array(self, size):
        if size == self.size:
            return self.array
        elif size > self.size:
            if size % self.size != 0:
                print("Error: attempt to scale base array unevenly.")
                return

            # duplicate the array until it's the right size.
            # retain the new, larger array in the object's data
            self.array = self.array*int(size/self.size)

            return self.array
        elif size < self.size:
            return self.array[0:size]
            # do not mutate the object's array in this case. Retain max array possible.

class InputArray(object):
    def __init__(self, size, array_ref, target=9):
        self.array_size = size
        self.target = target
        self.halfway = floor(self.target / 2)

        # Use base_array object to create arbitrary-size array
        self.array = array_ref.get_array(size)

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

def runtime_calc(input_array, trials, alg):
    mytest = Test(input_array)

    runtimes = []
    for n in range(trials):
        runtimes.append(mytest.run_test(alg))

    avg_runtime = sum(runtimes)/len(runtimes)
    return avg_runtime


def runtime_plot(trials):
    input_sizes = [100, 500, 1000]

    runtime_results = [[], [], []]

    # initialize base array to use as basis for all inputs
    base_array = BaseArray()

    for alg in [0, 1, 2]:
        for size in input_sizes:
            myarray = InputArray(size, base_array)
            runtime_results[alg].append(runtime_calc(myarray, trials, alg))

    plt.plot(input_sizes, runtime_results[0], label='basic (range)')
    plt.plot(input_sizes, runtime_results[1], label='enumerate')
    plt.plot(input_sizes, runtime_results[2], label='hash table')

    plt.xlabel('Input Size')
    plt.ylabel('Avg Runtime (s)')
    plt.title("Runtime vs. Input Size")
    plt.legend()

    plt.show()









#
