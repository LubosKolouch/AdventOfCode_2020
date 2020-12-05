#!/bin/env python
""" Advent Of Code 2020 Day 5 """
from collections import defaultdict


def decode_row(inp: str):
    """ decode the row and column """
    inp = inp.replace('F', '0')
    inp = inp.replace('B', '1')
    inp = inp.replace('L', '0')
    inp = inp.replace('R', '1')

    return int(inp[0:7], 2)*8+int(inp[7:], 2)


class Day5:
    """ Day5 tasks processor """

    def __init__(self):
        """ init day 5 """
        self.all_seats = defaultdict(int)

    def load_dict(self, input_file):
        """ Load the input dict """
        with open(input_file, "r") as in_file:
            for line in in_file.readlines():
                self.all_seats[decode_row(line.strip())] = 1

    def get_task1(self):
        """ get the numbers needed for Task1 """
        return max(self.all_seats.keys())

    def get_task2(self):
        """ get the numbers needed for Task2 """
        for seat in range(128*8):
            if not self.all_seats[seat] and self.all_seats[seat-1] and self.all_seats[seat+1]:
                return seat

        return None


def main():
    """ Run the daily tasks """
    day5 = Day5()
    day5.load_dict("input5")
    print(f"Task1: {day5.get_task1()}")
    print(f"Task2: {day5.get_task2()}")


if __name__ == "__main__":
    main()

day5_test = Day5()
day5_test.load_dict("input5")

assert decode_row("BFFFBBFRRR") == 567
assert decode_row("FFFBBBFRRR") == 119
assert decode_row("BBFFBBFRLL") == 820
