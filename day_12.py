#!/bin/env python
""" Advent of Code Day 12 """
import re
from collections import deque


class Day12:
    """ Class for processing of day 12 """

    def __init__(self):
        self.lines = []
        self.facing = "E"
        self.position = (0, 0)
        self.waypoint = (-1, 10)

        self.move_instr = {
                'N': (-1, 0),
                'S': (1, 0),
                'E': (0, 1),
                'W': (0, -1)
                }

        self.turn_instr = deque('ESWN')

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            self.lines = [line.rstrip('\n') for line in in_file]

    def get_task1(self):
        """ Navigate the ship """

        for line in self.lines:
            instr, step = re.match(r'(.)(\d+)', line).groups()
            step = int(step)

            if instr == "R":
                self.turn_instr.rotate(-step // 90)
                self.facing = self.turn_instr[0]
                continue

            if instr == "L":
                self.turn_instr.rotate(step // 90)
                self.facing = self.turn_instr[0]
                continue

            if instr == "F":
                instr = self.facing

            self.position = (self.position[0] + self.move_instr[instr][0] * step,
                             self.position[1] + self.move_instr[instr][1] * step)

        print(f"Task1: {abs(self.position[0]) + abs(self.position[1])}")
        return abs(self.position[0]) + abs(self.position[1])

    def get_task2(self):
        """ Navigate the ship and the waypoint """
        self.facing = "E"
        self.position = (0, 0)
        self.waypoint = (-1, 10)

        for line in self.lines:
            instr, step = re.match(r'(.)(\d+)', line).groups()
            step = int(step)

            if instr == "R":
                rotations = 4 - (step // 90)

                for _ in range(rotations):
                    self.waypoint = (-self.waypoint[1], self.waypoint[0])
                continue

            if instr == "L":
                rotations = step // 90

                for _ in range(rotations):
                    self.waypoint = (-self.waypoint[1], self.waypoint[0])
                continue

            if instr == "F":
                self.position = (self.position[0] + self.waypoint[0] * step,
                                 self.position[1] + self.waypoint[1] * step)
                continue

            self.waypoint = (self.waypoint[0] + self.move_instr[instr][0] * step,
                             self.waypoint[1] + self.move_instr[instr][1] * step)

        print(f"Task2: {abs(self.position[0]) + abs(self.position[1])}")
        return abs(self.position[0]) + abs(self.position[1])


def test_app():
    """ Run the tests """
    runner = Day12()
    runner.load_input("input12_test")
    assert runner.get_task1() == 25


if __name__ == "__main__":
    day_processor = Day12()
    day_processor.load_input("input12")
    task1 = day_processor.get_task1()
    task2 = day_processor.get_task2()
