#!/bin/env python
""" Advent of Code Day 7 """
import re
from collections import deque


class Day7:
    """ Class for processing of day 7 """
    def __init__(self):
        self.all_lines = ()
        self.all_bags = {}

    def load_input(self, file_name):
        """ Load the input file """
        with open(file_name, "r") as in_file:
            self.all_lines = [line.rstrip('\n') for line in in_file]

    def process_lines(self):
        """ Process all lines, load the mapping """

        for line in self.all_lines:
            container_re = re.compile(r'(.*?) bags')
            bags_re = re.compile(r'(?:(\d+)|no other) (.*?) bags*')
            container_name = re.match(container_re, line).group(1)
            bags = re.findall(bags_re, line)
            self.all_bags[container_name] = bags

    def get_task1(self):
        """ Find all bags that contain the golden one """
        gold_containers = set()
        queue = deque()
        queue.append('shiny gold')

        while queue:
            test_name = queue.pop()
            for container_name, items in self.all_bags.items():
                for _, bag in items:
                    if test_name in bag:
                        queue.append(container_name)
                        gold_containers.add(container_name)

        return len(gold_containers)

    def count_containers(self, container_name):
        """ Recursively count the containers """

        count = 1
        for name, items in self.all_bags.items():
            if container_name in name:
                for bag_count, bag in items:
                    count += int(bag_count) * self.count_containers(bag)

        return count

    def get_task2(self):
        """ Count all bags within the shiny gold one """

        return self.count_containers('shiny gold') - 1


if __name__ == "__main__":
    day7 = Day7()
    day7.load_input("input7")
    day7.process_lines()
    print(f"Task1: {day7.get_task1()}")
    print(f"Task2: {day7.get_task2()}")
