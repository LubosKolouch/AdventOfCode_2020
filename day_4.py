#!/bin/env python
""" Advent Of Code 2020 Day 4 """
import re


class Passport:
    """ Everything about the passports """
    mandatory_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    def __init__(self):
        self.fields = {}

    def check_byr(self):
        """ Check the rules for byr """

        if re.match(r'(19[2-9]\d)|(200[012]$)', self.fields['byr']):
            return 1

        return 0

    def check_iyr(self):
        """ Check the rules for iyr """

        if re.match(r'20[12]\d$', self.fields['iyr']):
            return 1

        return 0

    def check_eyr(self):
        """ Check the rules for eyr """

        if re.match(r'20[23]\d$', self.fields['eyr']):
            return 1

        return 0

    def check_hgt(self):
        """ Check the rules for hgt """

        match = re.match(r'(\d+)(cm|in)$', self.fields['hgt'])
        if not match:
            return 0

        if match.group(2) == 'cm' and 193 >= int(match.group(1)) >= 150:
            return 1

        if match.group(2) == 'in' and 76 >= int(match.group(1)) >= 59:
            return 1

        return 0

    def check_hcl(self):
        """ Check the rules for hcl """
        match = re.match(r'#([0-9]|[a-f]){6}$', self.fields['hcl'])
        if not match:
            return 0

        return 1

    def check_ecl(self):
        """ Check the rules for ecl """

        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not self.fields['ecl'] in valid_colors:
            return 0

        return 1

    def check_pid(self):
        """ Check the rules for pid """
        match = re.match(r'([0-9]){9}$', self.fields['pid'])
        if not match:
            return 0

        return 1

    def is_valid(self, task: int):
        """ Check if the given passport is valid """
        for field in self.mandatory_fields:
            if not self.fields.get(field, ''):
                return 0

            if task == 2:
                check_func = f"check_{field}"
                func = getattr(self, check_func)
                if not func():
                    return 0

        return 1


class Day4:
    """ Day4 tasks processor """

    def __init__(self):
        """ init day 4 """
        self.passports = []

    def load_dict(self, input_file):
        """ Load the input dict """
        with open(input_file, "r") as in_file:
            for l_count, line in enumerate(in_file.readlines()):
                line = line.strip()

                if l_count == 0 or line == "":
                    passport = Passport()
                    self.passports.append(passport)

                if line:
                    fields = line.split(' ')
                    for field in fields:
                        item, value = field.split(':')
                        passport.fields[item] = value

    def get_valid_passports(self, task: int):
        """ Count valid passports """
        valid_passports = 0
        for passport in self.passports:
            if passport.is_valid(task=task):
                valid_passports += 1

        return valid_passports

    def get_task1(self):
        """ get the numbers needed for Task1 """
        return self.get_valid_passports(task=1)

    def get_task2(self):
        """ get the numbers needed for Task2 """
        return self.get_valid_passports(task=2)


def main():
    """ Run the daily tasks """
    day4 = Day4()
    day4.load_dict("input4")
    print(f"Task1: {day4.get_task1()}")
    print(f"Task2: {day4.get_task2()}")


if __name__ == "__main__":
    main()

day4_test = Day4()
day4_test.load_dict("input4")

test_passport = Passport()
test_passport.fields['byr'] = '2002'
assert test_passport.check_byr() == 1
test_passport.fields['byr'] = '2003'
assert test_passport.check_byr() == 0
test_passport.fields['byr'] = 'abcd'
assert test_passport.check_byr() == 0
test_passport.fields['byr'] = 'a2003'
assert test_passport.check_byr() == 0
test_passport.fields['byr'] = '1919'
assert test_passport.check_byr() == 0
test_passport.fields['byr'] = '0002'
assert test_passport.check_byr() == 0

test_passport.fields['hgt'] = '60in'
assert test_passport.check_hgt() == 1
test_passport.fields['byr'] = '190cm'
assert test_passport.check_hgt() == 1
test_passport.fields['hgt'] = '190in'
assert test_passport.check_hgt() == 0
test_passport.fields['hgt'] = '190'
assert test_passport.check_hgt() == 0

test_passport.fields['hcl'] = '#123abc'
assert test_passport.check_hcl() == 1
test_passport.fields['hcl'] = '#123abz'
assert test_passport.check_hcl() == 0
test_passport.fields['hcl'] = '123abc'
assert test_passport.check_hcl() == 0
test_passport.fields['hcl'] = '#123abca'
assert test_passport.check_hcl() == 0

test_passport.fields['ecl'] = 'brn'
assert test_passport.check_ecl() == 1
test_passport.fields['ecl'] = 'wat'
assert test_passport.check_ecl() == 0
test_passport.fields['ecl'] = 'wata'
assert test_passport.check_ecl() == 0

test_passport.fields['pid'] = '000000001'
assert test_passport.check_pid() == 1
test_passport.fields['pid'] = '0123456789'
assert test_passport.check_pid() == 0
test_passport.fields['pid'] = 'a000000001'
assert test_passport.check_pid() == 0
