#!/bin/env python
""" Advent of Code Day 17 """
from collections import Counter
from copy import deepcopy
from itertools import product


# TODO : Speed-up as the levels are symmetric... no need to process twice.
class Day17:
    """ Class for processing of day 17 """

    def __init__(self, task: int = 1):
        self.cubes = dict()
        self.new_cubes = dict()
        self.task = task

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            lines = [line.rstrip('\n') for line in in_file]
            for line_nr, line in enumerate(lines):
                for char_nr, char in enumerate(line):
                    if self.task == 1:
                        self.cubes[(0, line_nr, char_nr)] = char
                    else:
                        self.cubes[(0, 0, line_nr, char_nr)] = char

    def get_visible_cubes(self, position):
        """ Get all the visible cubes from a position """
        visible_cubes = []

        all_changes = product([-1, 0, 1], repeat=self.task+2)

        for change in all_changes:
            zeroes = Counter(change)
            if zeroes[0] == self.task+2:
                continue

            res_pos = tuple([sum(x) for x in zip(change, position)])
            visible_cubes.append(res_pos)

        return visible_cubes

    def get_active_count(self, position) -> int:
        """ Count the active neighbours """

        total_active = 0
        visible_cubes = self.get_visible_cubes(position)

        for seat in visible_cubes:
            if self.cubes.get(seat, '.') == "#":
                total_active += 1

        return total_active

    @property
    def get_task(self) -> int:
        """ Run the Game of Life """

        my_round = 0

        while my_round < 6:

            self.new_cubes = dict()

            for seat in self.cubes.keys():
                self.new_cubes[seat] = self.cubes[seat]
                visible_cells = self.get_visible_cubes(seat)
                for cell in visible_cells:
                    if self.cubes.get(cell, -1) == -1:
                        self.new_cubes[cell] = "."
                    else:
                        self.new_cubes[cell] = self.cubes[cell]

            self.cubes = deepcopy(self.new_cubes)
            for seat in self.cubes.keys():
                active_cubes = self.get_active_count(seat)
                if self.cubes[seat] == "#" and active_cubes not in [2, 3]:
                    self.new_cubes[seat] = "."

                elif self.cubes[seat] == "." and active_cubes == 3:
                    self.new_cubes[seat] = "#"

            self.cubes = deepcopy(self.new_cubes)
            cubes_counter = Counter(self.cubes.values())
            print(f"Counter: {Counter(self.cubes.values())}")
            my_round += 1

        cubes_counter = Counter(self.cubes.values())
        print(f"Task{self.task}: {cubes_counter}")
        return cubes_counter['#']


def test_app():
    """ Run the tests """
    runner = Day17()
    runner.load_input("input17_test")
    task1_solution = runner.get_task
    assert task1_solution == 112

    runner = Day17(task=2)
    runner.load_input("input17_test")
    task1_solution = runner.get_task
    assert task1_solution == 848


if __name__ == "__main__":
    day_processor = Day17()
    day_processor.load_input("input17")
    task1 = day_processor.get_task

    task2 = Day17(task=2)
    task2.load_input("input17")
    result = task2.get_task
