#!/bin/env python
""" Advent Of Code 2020 Day 1 """


class Day1:
    """ Day1 tasks processor """

    def __init__(self, in_arr):
        """ load the input """
        self.in_arr = sorted(in_arr)

    def get_sum_two_2020(self):
        """ get the numbers needed for Task1 """

        # loop throught the list
        # check if the numbers add to 2020
        # exit the loop if over 2020
        for pos, num in enumerate(self.in_arr):
            if 2020-num in self.in_arr[pos+1:]:
                return num*(2020-num)

        return None

    def get_sum_three_2020(self):
        """ get the numbers needed for Task2 """

        for pos, num in enumerate(self.in_arr):
            for pos2, num2 in enumerate(self.in_arr[pos+1:]):
                if num+num2 > 2020:
                    break

                if 2020-num-num2 in self.in_arr[pos2+1:]:
                    return num*num2*(2020-num-num2)

        return None


def main():
    """ Run the daily tasks """
    with open("input1", "r") as in_file:
        in_arr = (int(line.strip()) for line in in_file.readlines())

    day1 = Day1(in_arr)
    print(f"Task1: {day1.get_sum_two_2020()}")
    print(f"Task2: {day1.get_sum_three_2020()}")


if __name__ == "__main__":
    main()

day1_test = Day1([2000, 2, 20, 10, 10])
assert day1_test.get_sum_two_2020() == 2000*20
assert day1_test.get_sum_three_2020() == 2000*10*10

day2_test = Day1([1010, 810, 200, 10, 10])
assert day2_test.get_sum_two_2020() is None
assert day2_test.get_sum_three_2020() == 1010*810*200
