#!/bin/env python
""" Advent of Code Day 15 """
from collections import defaultdict, deque


class Day15:
    """ Class for processing of day 15 """

    def __init__(self):
        self.lines = []
        self.seen_nums = {}

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            for line in in_file.readlines():
                for num in line.rstrip('\n').split(','):
                    self.lines.append(int(num))

    def get_task(self, limit: int):
        """ Play the memory numbers game """

        self.seen_nums = defaultdict(deque)
        turn = 0
        num_queue = deque(self.lines)

        while turn < len(self.lines):
            turn += 1

            num = num_queue.popleft()
            self.seen_nums[num].append(turn)

        turn += 1

        self.seen_nums[0].append(turn)
        num = 0

        while turn < limit:
            turn += 1

            next_num = 0
            if len(self.seen_nums[num]) > 1:
                next_num = self.seen_nums[num][1] - self.seen_nums[num][0]

            num = next_num
            self.seen_nums[next_num].append(turn)

            if len(self.seen_nums[next_num]) > 2:
                self.seen_nums[next_num].popleft()

        print(f"Task: {num}")
        return num


def test_app():
    """ Run the tests """
    runner = Day15()
    runner.load_input("input15_test")
    assert runner.get_task(limit=10) == 0
    assert runner.get_task(limit=30000000) == 175594


if __name__ == "__main__":
    day_processor = Day15()
    day_processor.load_input("input15")
    task1 = day_processor.get_task(limit=2020)
    task2 = day_processor.get_task(limit=30000000)
