#!/bin/env python
""" Advent Of Code 2020 Day 2 """
import re


class Day3:
    """ Day3 tasks processor """

    def __init__(self):
        """ init day 3 """
        self.in_dict = {}
        self.max_line = 0
        self.max_col = 0

    def load_dict(self, input_file):
        """ Load the input dict """
        with open(input_file, "r") as in_file:
            for l_count, line in enumerate(in_file.readlines()):
                self.max_line = max(l_count, self.max_line)

                self.max_col = len(line)-1
                for c_count, char in enumerate(line):
                    self.in_dict[(l_count, c_count)] = char

    def traverse_slope(self, line_step: int, col_step: int):
        """ Traverse the slope in given order """
        trees_count = 0
        line_pos = col_pos = 0
        while line_pos <= self.max_line - line_step:
            line_pos += line_step
            col_pos = (col_pos + col_step) % self.max_col
            if self.in_dict[(line_pos, col_pos)] == "#":
                trees_count += 1

        return trees_count

    def get_task1(self):
        """ get the numbers needed for Task1 """
        return self.traverse_slope(1, 3)

    def get_task2(self):
        """ get the numbers needed for Task1 """

        slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

        trees_count = 1

        for slope in slopes:
            trees_count *= self.traverse_slope(slope[1], slope[0])

        return trees_count


def main():
    """ Run the daily tasks """
    day3 = Day3()
    day3.load_dict("input3")
    print(f"Task1: {day3.get_task1()}")
    print(f"Task2: {day3.get_task2()}")


if __name__ == "__main__":
    main()

day3_test = Day3()
day3_test.load_dict("input3")

assert day3_test.get_task1() == 257
assert day3_test.get_task2() == 1744787392
