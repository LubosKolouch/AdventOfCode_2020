#!/bin/env python
""" Advent of Code Day 21 """
from collections import defaultdict, Counter
from copy import deepcopy


class Day21:
    """ Class for processing of day 21 """

    def __init__(self):
        self.allergens = defaultdict(list)
        self.bad_food = {}
        self.all_food = []
        self.aller_map = {}

    def load_input(self, file_name):
        """ load the input """

        with open(file_name, "r") as in_file:
            for line in in_file.readlines():
                ingr, aller = line.rstrip("\n").replace(')', '').split('(contains ')
                ingr_list = (ingr.split(' '))
                for item in ingr_list[:-1]:
                    self.all_food.append(item)
                for one_aller in aller.split(', '):
                    self.allergens[one_aller].append(set(ingr_list[:-1]))

    @property
    def get_task1(self):
        """ Process the rules """
        for aller in self.allergens:
            intersect = set.intersection(*self.allergens[aller])
            self.aller_map[aller] = intersect
            for food in intersect:
                self.bad_food[food] = 1

        total = 0

        for item, count in Counter(self.all_food).items():
            if item in self.bad_food:
                continue
            total += count

        return total

    @property
    def get_task2(self):
        """ Process the rules """

        known_food = {}

        has_change = 1
        while has_change:
            has_change = 0
            new_map = deepcopy(self.aller_map)
            for item in self.aller_map:
                if len(self.aller_map[item]) == 1:
                    has_change = 1
                    known_food[self.aller_map[item].pop()] = item
                    del new_map[item]
                    break

                for food in self.aller_map[item]:
                    if food in known_food.keys():
                        new_map[item].remove(food)
                        has_change = 1
                        break
            self.aller_map = deepcopy(new_map)

        sort_food = [key for (key, value) in sorted(known_food.items(), key=lambda x: x[1])]
        result = ','.join(sort_food)
        return result


def test_app():
    """ Run the tests """
    runner = Day21()
    runner.load_input("input21_test")
    assert runner.get_task1 == 5
    assert runner.get_task2 == 'mxmxvkd,sqjhc,fvjkl'


if __name__ == "__main__":
    day_processor = Day21()
    day_processor.load_input("input21")
    print(f"Task1: {day_processor.get_task1}")
    print(f"Task2: {day_processor.get_task2}")
