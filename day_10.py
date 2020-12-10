#!/bin/env python
""" Advent of Code Day 10 """
from collections import defaultdict


class Day10:
    """ Class for processing of day 10 """
    def __init__(self):
        self.numbers = []
        self.jolt_diffs = defaultdict(int)

    def load_input(self, file_name):
        """ load the input """
        with open(file_name, "r") as in_file:
            self.numbers = [int(line.rstrip('\n')) for line in in_file]

        self.numbers.sort()

    def get_task1(self):
        """ Find joltage differences """

        prev_num = 0

        for item in self.numbers:
            self.jolt_diffs[item - prev_num] += 1
            prev_num = item

        # my device
        self.jolt_diffs[3] += 1

        print(f"Task1 : {self.jolt_diffs[1] * self.jolt_diffs[3]}")
        return self.jolt_diffs[1] * self.jolt_diffs[3]

    def get_task2(self, position: int = 0):
        """ Count the possible adapter combinations """

        paths = defaultdict(int)
        paths[0] = 1

        for item in self.numbers:
            paths[item] = paths[item-1] + paths[item-2] + paths[item-3]

        print(f"Task2 : {paths[self.numbers[-1]]}")
        return paths[self.numbers[-1]]


def test_app():
    """ Run the tests """
    runner = Day10()

    runner.load_input("input10_test1")
    print(runner.numbers)
    task1_solution = runner.get_task1()
    task2_solution = runner.get_task2()
    assert task1_solution == 7*5
    assert task2_solution == 8

    runner = Day10()
    runner.load_input("input10_test2")
    task1_solution = runner.get_task1()
    task2_solution = runner.get_task2()
    assert task1_solution == 22*10
    assert task2_solution == 19208


if __name__ == "__main__":
    day_processor = Day10()
    day_processor.load_input("input10")
    task1 = day_processor.get_task1()
    task2 = day_processor.get_task2()
