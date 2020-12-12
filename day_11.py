#!/bin/env python
""" Advent of Code Day 11 """
from collections import Counter, defaultdict
from copy import copy, deepcopy
from functools import cache


class Day11:
    """ Class for processing of day 11 """
    def __init__(self, task: int):
        self.seats = dict()

        self.task = task

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            lines = [line.rstrip('\n') for line in in_file]
            for line_nr, line in enumerate(lines):
                for char_nr, char in enumerate(line):
                    self.seats[(line_nr, char_nr)] = char
                    

    @cache
    def get_visible_seats(self, position):
        """ Get all the visible seats from a position """
        directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        visible_seats = []

        x_pos, y_pos = position
        for direction in directions:
            x_offset, y_offset = direction

            x_new_pos = x_pos + x_offset
            y_new_pos = y_pos + y_offset

            while self.seats.get((x_new_pos, y_new_pos), 0):

                if self.seats[(x_new_pos, y_new_pos)] != ".":
                    visible_seats.append((x_new_pos, y_new_pos))
                    break

                if self.task == 1:
                    break

                x_new_pos = x_new_pos + x_offset
                y_new_pos = y_new_pos + y_offset

        return visible_seats

    def get_occupied_count(self, position):
        """ Count the active neighbours """

        total_occupied = 0
        visible_seats = self.get_visible_seats(position)

        for seat in visible_seats:
            if self.seats[seat] == "#":
                total_occupied += 1

        return total_occupied

    def get_task(self):
        """ Run the Game of Life """

        has_change = 1

        needed_seats = {1: 4, 2: 5}

        while has_change == 1:
            new_seats = copy(self.seats)
            has_change = 0
            for seat in self.seats.keys():
                occupied_seats = self.get_occupied_count(seat)
                if self.seats[seat] == "L" and occupied_seats == 0:
                    new_seats[seat] = "#"
                    has_change = 1

                elif self.seats[seat] == "#" and occupied_seats >= needed_seats[self.task]:
                    new_seats[seat] = "L"
                    has_change = 1

            self.seats = deepcopy(new_seats)
            seats_counter = Counter(self.seats.values())
        seats_counter = Counter(self.seats.values())
        print(f"Task{self.task}: {seats_counter}")
        return seats_counter['#']


def test_app():
    """ Run the tests """
    runner = Day11(task=1)
    runner.load_input("input11_test")
    task1_solution = runner.get_task()

    runner = Day11(task=2)
    runner.load_input("input11_test")
    task2_solution = runner.get_task()
    assert task1_solution == 37
    assert task2_solution == 26


if __name__ == "__main__":
    day_processor = Day11(1)
    day_processor.load_input("input11")
    task1 = day_processor.get_task()
    day_processor = Day11(2)
    day_processor.load_input("input11")
    task2 = day_processor.get_task()
