#!/bin/env python
""" Advent of Code Day 14 """
import re
from collections import defaultdict
from itertools import product


class Day14:
    """ Class for processing of day 14 """

    def __init__(self):
        self.mem = defaultdict(int)
        self.mask = ''
        self.input = []

    def load_input(self, file_name):
        """ load the input """

        self.input = []
        with open(file_name, "r") as in_file:
            for line in in_file.readlines():
                self.input.append(line.strip('\n'))

    def get_task(self, task: int = 1):
        """ Get the values in the memory """

        self.mem = defaultdict(int)
        for line in self.input:
            line_parts = line.split(' = ')

            if line_parts[0] == "mask":
                self.mask = line_parts[1]
                continue

            addr, instr = re.findall(r'\d+', line)
            if task == 1:
                bin_addr = list("{0:{fill}36b}".format(int(instr), fill='0'))
                for pos, _ in enumerate(bin_addr):
                    if self.mask[pos] != "X":
                        bin_addr[pos] = self.mask[pos]

                self.mem[addr] = int(''.join(bin_addr), 2)
                continue

            bin_addr = "{0:{fill}36b}".format(int(addr), fill='0')

            bin_list = []
            x_count = max(1, self.mask.count("X"))

            all_masks = product('01', repeat=x_count)

            for mask in all_masks:
                bin_list.append(list(bin_addr))
                seen_x = 0
                for pos, _ in enumerate(bin_list[-1]):
                    if self.mask[pos] == "X":
                        bin_list[-1][pos] = mask[seen_x]
                        seen_x += 1
                    if self.mask[pos] == '1':
                        bin_list[-1][pos] = '1'

            for addr in bin_list:
                self.mem[int(('').join(addr), 2)] = int(instr)

        print(f"Task{task}: {sum(self.mem.values())}")
        return sum(self.mem.values())


def test_app():
    """ Run the tests """
    runner = Day14()
    runner.load_input("input14_test")
    assert runner.get_task() == 165
    runner.load_input("input14_test2")
    assert runner.get_task(task=2) == 208


if __name__ == "__main__":
    day_processor = Day14()
    day_processor.load_input("input14")
    task1 = day_processor.get_task()
    task2 = day_processor.get_task(task=2)
