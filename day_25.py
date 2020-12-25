#!/bin/env python
""" Advent of Code Day 25 """
from collections import Counter, defaultdict
from copy import deepcopy


class Day25:
    """ Class for processing of day 25 """
    def __init__(self):
        self.card_key = 0
        self.door_key = 0

        self.card_loops = {}
        self.door_loops = {}

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            lines = [line.rstrip('\n') for line in in_file]
            self.card_key = int(lines[0])
            self.door_key = int(lines[1])

    def get_loop_nr(self, public_key):
        """ do the loops """

        loops = 0
        value = 1
        while 1:
            loops += 1
            value = (value * 7) % 20201227

            if value == public_key:
                return loops

    def do_transform(self, key, times):
        """ Do the transformation """

        value = 1
        for i in range(1, times + 1):
            value = (value * key) % 20201227

        return value

    def get_task1(self):
        """ Get the encryption key """
        card_loop_nr = self.get_loop_nr(self.card_key)

        key = self.do_transform(self.door_key, card_loop_nr)
        print(f"Task1: {key}")
        return key

    def get_task2(self):
        """ Run the Game of Life """
        pass


def test_app():
    """ Run the tests """
    runner = Day25()
    runner.load_input("input25_test")
    task1_solution = runner.get_task1()
    assert task1_solution == 14897079

if __name__ == "__main__":
    day_processor = Day25()
    day_processor.load_input("input25")
    task1 = day_processor.get_task1()
