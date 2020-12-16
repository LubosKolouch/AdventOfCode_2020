#!/bin/env python
""" Advent of Code Day 16 """
# TODO: refactor code, put things to separate functions
import re


class Day16:
    """ Class for processing of day 16 """

    def __init__(self):
        self.lines = []
        self.rules = {}
        self.all_tickets = {}
        self.task2_tickets = {}

    def load_input(self, file_name):
        """ load the input """

        switch = 0
        counter = 1
        with open(file_name, "r") as in_file:
            for line in in_file.readlines():
                line = line.rstrip("\n")
                if line == "":
                    switch += 1
                    continue

                if switch == 0:
                    fields = re.findall(r'^(.*?)\:\s+(\d+)-(\d+)\s+or\s+(\d+)-(\d+)', line)
                    self.rules[fields[0][0]] = [(int(fields[0][1]), int(fields[0][2])),
                                                (int(fields[0][3]), int(fields[0][4]))]

                else:
                    if 'ticket' in line:
                        continue

                    fields = re.findall(r'(\d+)',  line)
                    self.all_tickets[counter] = list(map(int, fields))
                    self.task2_tickets[counter] = list(map(int, fields))
                    counter += 1

    @property
    def get_task1(self):
        """ Process the rules """
        invalid = 0

        for ticket_nr, ticket in self.all_tickets.items():
            if ticket_nr == 0:
                continue
            for number in ticket:
                is_valid = 0
                for rule in self.rules.values():
                    if is_valid:
                        break
                    for values in rule:
                        if values[1] >= number >= values[0]:
                            is_valid = 1
                            break

                if not is_valid:
                    invalid += number
                    if ticket_nr in self.task2_tickets:
                        self.task2_tickets.pop(ticket_nr)

        print(f"Task1: {invalid}")
        return invalid

    def get_task2(self, word):
        """ Process the rules """

        all_combs = {}

        # create a dict with all possible fields for each column
        for i in range(len(self.rules)):
            all_combs[i] = [rule for rule in self.rules]

        # filter out invalid values
        for value in self.task2_tickets.values():
            for pos, number in enumerate(value):
                for rule_candidate in all_combs[pos]:
                    is_valid = 0
                    for values in self.rules[rule_candidate]:
                        if values[1] >= number >= values[0]:
                            is_valid = 1
                            break
                    if is_valid == 0:
                        all_combs[pos].remove(rule_candidate)

        # backtrack and delete multiple values
        changed = 1

        while changed:
            changed = 0
            for comb in all_combs:
                if len(all_combs[comb]) == 1:
                    # remove it from other fields
                    for comb2 in all_combs:
                        if comb2 == comb:
                            continue

                        if len(all_combs[comb2]) > 1:
                            changed = 1
                            if all_combs[comb][0] in all_combs[comb2]:
                                all_combs[comb2].remove(all_combs[comb][0])

        # get departure fields
        departure_fields = []

        for item in all_combs:
            if word in all_combs[item][0]:
                departure_fields.append(item)

        # get the sum
        total = 1
        for item in departure_fields:
            total *= self.all_tickets[1][item]

        print(f"Task2: {total}")
        return total


def test_app():
    """ Run the tests """
    runner = Day16()
    runner.load_input("input16_test")
    assert runner.get_task1 == 71
    assert runner.get_task2('class') == 1


if __name__ == "__main__":
    day_processor = Day16()
    day_processor.load_input("input16")
    task1 = day_processor.get_task1
    task2 = day_processor.get_task2('departure')
