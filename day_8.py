#!/bin/env python
""" Advent of Code Day 8 """
from collections import defaultdict


class Day8:
    """ Class for processing of day 8 """
    def __init__(self, code):
        self.code = code
        self.seen_lines = defaultdict(int)
        self.code_pos = 0
        self.acc = 0

    def process_lines(self):
        """ Process all lines, load the mapping """

        while 1:
            if self.seen_lines[self.code_pos]:
                return 0

            self.seen_lines[self.code_pos] = 1

            try:
                instr, count = self.code[self.code_pos].split(' ')
            except IndexError:
                return 1

            if instr == "acc":
                self.acc += int(count)

            if instr == "jmp":
                self.code_pos += int(count)
                continue

            self.code_pos += 1

    def get_task1(self):
        """ Find all bags that contain the golden one """
        self.process_lines()
        return self.acc

    def get_task2(self):
        """ Find all bags that contain the golden one """
        return self.acc if self.process_lines() else 0


class TaskRunner:
    """ Run the tasks with a fresh day """

    def __init__(self):
        self.code = []

    def load_input(self, file_name):
        """ Load the input file """
        with open(file_name, "r") as in_file:
            self.code = [line.rstrip('\n') for line in in_file]

    def run_task1(self):
        """ Get answer for the task 1 """
        day8 = Day8(self.code)
        day8.process_lines()
        print(f"Task1: {day8.get_task1()}")

    def run_task2(self):
        """ Get asnwer for the task 2 """

        for line_pos, line in enumerate(self.code):
            if line.startswith('jmp') or line.startswith('nop'):
                new_code = self.code.copy()

                if line.startswith('jmp'):
                    new_code[line_pos] = new_code[line_pos].replace('jmp', 'nop')
                else:
                    new_code[line_pos] = new_code[line_pos].replace('nop', 'jmp')

                day8 = Day8(new_code)
                result = day8.get_task2()
                if result:
                    print(f"Task2: {day8.acc}")


if __name__ == "__main__":
    task_runner = TaskRunner()
    task_runner.load_input("input8")
    task_runner.run_task1()
    task_runner.run_task2()
