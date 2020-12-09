#!/bin/env python
""" Advent of Code Day 9 """
from itertools import combinations


class Day9:
    """ Class for processing of day 9 """
    def __init__(self, preamble):
        self.numbers = []
        self.sums = set()
        self.preamble = preamble

    def get_sums(self, position):
        """ Fill in the sums set for previous 25 numbers """
        self.sums = set()
        for comb in combinations(self.numbers[position-self.preamble: position], 2):
            self.sums.add(sum(comb))

    def load_input(self, file_name):
        """ load the input """
        with open(file_name, "r") as in_file:
            self.numbers = [int(line.rstrip('\n')) for line in in_file]

    def get_task1(self):
        """ Find the first number that is not valid """
        for position, line in enumerate(self.numbers[self.preamble:]):
            self.get_sums(position+self.preamble)
            if line not in self.sums:
                print(f"Task1: {line}")
                return line

        return 0

    def get_task2(self, target_sum: int):
        """ Find the smallest and largest number in a list producing the required sum """

        for pos, line in enumerate(self.numbers):
            list_sum = line
            # loop through the list until a match is found or over the target

            for offset, line2 in enumerate(self.numbers[pos+1:]):
                offset += 1
                list_sum += line2

                if list_sum == target_sum:
                    min_value = min(self.numbers[pos:offset+pos+1])
                    max_value = max(self.numbers[pos:offset+pos+1])

                    print(f"Task2: {min_value+max_value}")
                    return min_value+max_value

                if list_sum > target_sum:
                    break

        return 0


def test_app():
    """ Run the tests """
    runner = Day9(5)
    runner.load_input("input9_test")
    task1_solution = runner.get_task1()
    assert task1_solution == 127
    assert runner.get_task2(task1_solution) == 62


if __name__ == "__main__":
    day_processor = Day9(25)
    day_processor.load_input("input9")
    task1 = day_processor.get_task1()
    day_processor.get_task2(task1)
