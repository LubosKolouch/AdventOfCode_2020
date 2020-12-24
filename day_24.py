#!/bin/env python
""" Advent of Code Day 24 """
from collections import Counter, defaultdict
from copy import deepcopy


class Day24:
    """ Class for processing of day 24 """

    directions = {
        'e': (1, 0),
        'se': (1, 1),
        'sw': (0, 1),
        'w': (-1, 0),
        'nw': (-1, -1),
        'ne': (0, -1)
    }

    def __init__(self):
        self.lines = []
        self.tiles = defaultdict(int)

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            self.lines = [line.rstrip('\n') for line in in_file]

    def walk_the_array(self, instr_list):
        """ Get all the visible seats from a position """

        coord = [0, 0]
        iter_lines = iter(instr_list)
        while True:
            try:
                instr = next(iter_lines)

                if instr in ['n', 's']:
                    instr += next(iter_lines)

                offset = self.directions[instr]

                coord[0] += offset[0]
                coord[1] += offset[1]

            except StopIteration:
                break

        self.tiles[tuple(coord)] = 0 if self.tiles[tuple(coord)] == 1 else 1

    def expand_tiles(self):
        """ Expand the field """

        new_tiles = deepcopy(self.tiles)
        for tile_coord in new_tiles:
            for direction in self.directions.values():
                _ = self.tiles[tuple((tile_coord[0] + direction[0],
                                      tile_coord[1] + direction[1]))]

    def run_game(self, tiles):
        """ Game of Life """

        for tile_coord in tiles:
            count_black = 0
            for direction in self.directions.values():
                if tiles.get(
                        tuple((tile_coord[0] + direction[0],
                               tile_coord[1] + direction[1])), 0) == 1:
                    count_black += 1

            if tiles[tile_coord] == 1 and (count_black == 0
                                           or count_black > 2):
                self.tiles[tile_coord] = 0

            if tiles[tile_coord] == 0 and count_black == 2:
                self.tiles[tile_coord] = 1

    def get_task1(self):
        """ Load the array """

        for line in self.lines:
            self.walk_the_array(line)
        counter = Counter(self.tiles.values())

        print(f"Task1: {counter[1]}")
        return counter[1]

    def get_task2(self):
        """ Run the Game of Life """

        for _ in range(100):
            self.expand_tiles()

            new_array = deepcopy(self.tiles)
            self.run_game(new_array)

            counter = Counter(self.tiles.values())

        print(f"Task2: {counter[1]}")
        return counter[1]


def test_app():
    """ Run the tests """
    runner = Day24()
    runner.load_input("input24_test")
    task1_solution = runner.get_task1()
    assert task1_solution == 10
    task2_solution = runner.get_task2()
    assert task2_solution == 2208


if __name__ == "__main__":
    day_processor = Day24()
    day_processor.load_input("input24")
    task1 = day_processor.get_task1()
    task2 = day_processor.get_task2()
