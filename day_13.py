#!/bin/env python
""" Advent of Code Day 13 """
from math import inf, lcm
from itertools import count


class Day13:
    """ Class for processing of day 13 """

    def __init__(self):
        self.buses = {}
        self.arrival = 0

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            self.arrival = int(in_file.readline().strip('\n'))
            buses = in_file.readline().strip('\n')

            for bus_time, bus in enumerate(buses.split(',')):
                if bus != "x":
                    self.buses[bus_time] = int(bus)

    @property
    def get_task1(self):
        """ Wait for the bus """

        min_wait = inf
        min_wait_bus = 0

        for _, bus in self.buses.items():
            if self.arrival % bus == 0:
                return 0

            if (bus - self.arrival % bus) < min_wait:
                min_wait = bus - self.arrival % bus
                min_wait_bus = bus

        print(f"Task1: {min_wait * min_wait_bus}")

        return min_wait * min_wait_bus

    @property
    def get_task2(self):
        """ Find the periods when the buses arrive within 1 minute """

        time = 0
        step = self.buses[0]
        for minute, period in self.buses.items():

            if minute == 0:
                continue
            for time in count(time, step):
                if (time + minute) % period == 0:
                    break

            step = lcm(step, period)

        print('Task2:', time)
        return time


def test_app():
    """ Run the tests """
    runner = Day13()
    runner.load_input("input13_test")
    assert runner.get_task1 == 295
    assert runner.get_task2 == 1068781


if __name__ == "__main__":
    day_processor = Day13()
    day_processor.load_input("input13")
    task1 = day_processor.get_task1
    task2 = day_processor.get_task2
