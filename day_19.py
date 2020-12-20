#!/bin/env python
""" Advent of Code Day 19 """
import re
from copy import deepcopy


def convert_rule_to_regex(rule):
    """ Take a rule and convert it to a regex """
    print(f"a {rule}")
    rule = rule.replace('"', '')
    parts = rule.strip().split('|')

    for part_nr, part in enumerate(parts):
        if not re.search(r'\d', part):
            parts[part_nr] = f"{part.strip()}"
        else:
            parts[part_nr] = f"({part.strip()})"

    if len(parts) == 1:
        rule = parts[0]
    else:
        rule = "( " + '|'.join(parts) + " )"

    return rule


class Day19:
    """ Class for processing of day 19 """
    def __init__(self, task: int=1) -> None:
        self.msg_rules = {}
        self.messages = []
        self.conv_rules = {}

    def load_input(self, file_name) -> None:
        """ load the input """

        with open(file_name, "r") as in_file:
            seen_empty = 0

            rules = {}

            for line in in_file:
                line = line.rstrip('\n')
                if line == "":
                    seen_empty = 1
                    continue

                if seen_empty == 0:
                    rule_nr, content = line.strip().split(':')
                    content = content.strip()
                    rules[str(rule_nr)] = str(content)

                else:
                    self.messages.append(line.strip())

        self.msg_rules = deepcopy(rules)
        print(self.msg_rules)

    def process_rules(self) -> None:
        """ Convert the rules to characters
            Process the rules and convert it step by step """

        # first separate the | in the rules
        for rule_nr, rule in self.msg_rules.items():
            self.conv_rules[rule_nr] = convert_rule_to_regex(rule)

        # replace the rules until none is left

        #
        self.msg_rules = deepcopy(self.conv_rules)

        missing_elems = []
        for rule_nr, rule in self.msg_rules.items():
            nums = re.findall(r'\d+', rule)
            if nums:
                missing_elems.append(rule_nr)

        len_mis = len(missing_elems)
        while len_mis and re.search(r'\d', self.msg_rules['0']):

            for rule_nr in missing_elems:
                rule = self.msg_rules[rule_nr]
                if rule_nr == '24':
                    print(rule_nr)
                nums = re.findall(r'\d+', rule)

                for num in nums:
                    if not re.search(r'\d', self.msg_rules[num]):
                        self.msg_rules[rule_nr] = re.sub(r'\b'+num+r'\b', self.msg_rules[num], self.msg_rules[rule_nr])

            missing_elems = []
            for rule_nr, rule in self.msg_rules.items():
                nums = re.findall(r'\d+', rule)
                if nums:
                    missing_elems.append(rule_nr)

            len_mis = len(missing_elems)
            print(len_mis)
            # cleanup spaces
        new_rules = deepcopy(self.msg_rules)

        for rule_nr, rule in self.msg_rules.items():
            new_rules[rule_nr] = re.sub(r'\s+', '', rule)

        self.msg_rules = deepcopy(new_rules)
        print(f"4 {self.msg_rules}")

    @property
    def get_task(self) -> int:
        """ Solve the equations
        :rtype: int
        """

        self.process_rules()

        matches = 0
        look_regex = re.compile(self.msg_rules['0'])
        print(f"regex {look_regex}")
        for message in self.messages:
            if re.fullmatch(look_regex, message):
                matches += 1

        print(f"Task1: {matches}")
        return matches


def test_app():
    """ Run the tests """

    assert convert_rule_to_regex("4 1 5") == "(4 1 5)"
    assert convert_rule_to_regex("4 4 | 5 5") == "( (4 4)|(5 5) )"
    runner = Day19()
    runner.load_input("input19_test")
    assert runner.get_task == 2
    runner.load_input("input19_test2")
    assert runner.get_task == 2
    runner.load_input("input19_test3")
    assert runner.get_task == 3
    runner.load_input("input19_test3")
    runner.msg_rules['8'] =  ' 42 | 42 8 '
    runner.msg_rules['11'] = ' 42 31 | 42 11 31 '
    assert runner.get_task == 12



if __name__ == "__main__":
    day_processor = Day19()
    day_processor.load_input(
        "/home/lubos/sw/scripts/adventofcode/2020/input19")
    print(day_processor.get_task)
    day_processor.msg_rules['8'] =  ' 42 | 42 8 '
    day_processor.msg_rules['11'] = ' 42 31 | 42 11 31 '
    print(day_processor.get_task)

