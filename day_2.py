#!/bin/env python
""" Advent Of Code 2020 Day 2 """
import re
from collections import Counter


class Day2:
    """ Day2 tasks processor """

    def __init__(self, in_arr):
        """ load the input """
        self.in_arr = sorted(in_arr)
        self.re_task1 = re.compile(r'(\d+)-(\d+)\s+(.):\s+(.*)')

    def decode_line(self, line: str):
        """ get the values from the input file line """
        return self.re_task1.match(line).groups()

    def get_task1(self):
        """ get the numbers needed for Task1 """

        valid_passwords = 0
        # loop throught the list
        # count the letters
        # increase counter if matching the policy
        for pwd_line in self.in_arr:
            count_from, count_to, letter, pwd = self.decode_line(pwd_line)
            letters_count = Counter(pwd)
            if int(count_from) <= letters_count[letter] <= int(count_to):
                valid_passwords += 1

        return valid_passwords

    def get_task2(self):
        """ get the numbers needed for Task1 """

        valid_passwords = 0
        # loop throught the list
        # increase counter if only 1 letter at the right position
        for pwd_line in self.in_arr:
            pos1, pos2, letter, pwd = self.decode_line(pwd_line)
            letters_count = (pwd[int(pos1)-1] == letter) + (pwd[int(pos2)-1] == letter)
            if letters_count == 1:
                valid_passwords += 1

        return valid_passwords


def main():
    """ Run the daily tasks """
    with open("input2", "r") as in_file:
        in_arr = (line.strip() for line in in_file.readlines())

    day2 = Day2(in_arr)
    print(f"Task1: {day2.get_task1()}")
    print(f"Task2: {day2.get_task2()}")


if __name__ == "__main__":
    main()

day2_test = Day2(['4-5 l: rllllj', '1-2 l: rllllj'])
assert day2_test.decode_line('4-5 l: rllllj') == ('4', '5', 'l', 'rllllj')
assert day2_test.get_task1() == 1
assert day2_test.get_task2() == 1
