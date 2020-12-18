#!/bin/env python
""" Advent of Code Day 18 """
import re


class Num:
    """ A bit strange math needed for the exercises """

    def __init__(self, value) -> None:
        """
        A special number
        :type value: int
        """
        self.value = value

    def __sub__(self, other):
        """ redefine sub used for part 1 """
        return Num(self.value * other.value)

    def __and__(self, other):
        """ redefine the and use for part 2 """
        return Num(self.value * other.value)

    def __add__(self, other):
        """ add is used in both examples """
        return Num(self.value + other.value)

    @property
    def __int__(self):
        """ int is still a Num for adding """
        return Num(self.value)


class Day18:
    """ Class for processing of day 18 """

    def __init__(self, task: int = 1) -> None:
        self.lines = []
        self.task = task

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            self.lines = []
            for line in in_file:
                self.lines.append(line.rstrip('\n'))

    @property
    def get_task(self) -> int:
        """ Solve the equations
        :rtype: int
        """

        solution = Num(0)
        for line in self.lines:
            # - has the same priority as +
            # for part2, & has lower priority than +
            if self.task == 1:
                line = line.replace('*', '-')
            else:
                line = line.replace('*', '&')
            line = re.sub(r'(\d+)', r"Num(\1)", line)
            line_result = eval(line)
            solution += line_result

        print(f"Task{self.task}: {solution.value}")
        return solution.value


def test_app():
    """ Run the tests """
    runner = Day18()
    runner.load_input("input18_test")
    assert runner.get_task == 13632
    runner.task = 2
    assert runner.get_task == 23340


if __name__ == "__main__":
    day_processor = Day18()
    day_processor.load_input("input18")
    task1 = day_processor.get_task
    day_processor.task = 2
    task2 = day_processor.get_task
