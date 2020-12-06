#!/bin/env python
""" Advent of Code Day 6 """


def count_task1_group(answers):
    """ Return the answer for Task 1 """
    return len(set.union(*answers))


def count_task2_group(answers):
    """ Return the answer for Task 1 """
    return len(set.intersection(*answers))


def process_lines(lines):
    """ Process all lines in the input """
    total_task1 = 0
    total_task2 = 0
    answers = []
    for l_count, line in enumerate(lines):

        if line != "":
            answers.append(set(line.strip()))

        if line == "" or l_count == len(lines)-1:
            total_task1 += count_task1_group(answers)
            total_task2 += count_task2_group(answers)

            answers = []

    print(f"Task1: {total_task1}")
    print(f"Task2: {total_task2}")


with open("input6", "r") as in_file:
    all_lines = [line.rstrip('\n') for line in in_file]

process_lines(all_lines)

# TESTS #
with open("test_input6", "r") as in_file:
    all_lines = [line.rstrip('\n') for line in in_file]

process_lines(all_lines)


assert count_task1_group([set('abc')]) == 3
assert count_task1_group([set('a'), set('a'), set('b'), set('c')]) == 3

assert count_task1_group([set('ab'), set('ac')]) == 3
assert count_task1_group([set('a'), set('a'), set('a'), set('a')]) == 1
assert count_task1_group([set('abcx'), set('abcy'), set('abcz')]) == 6

assert count_task2_group([set('abc')]) == 3
assert count_task2_group([set('a'), set('a'), set('b'), set('c')]) == 0

assert count_task2_group([set('ab'), set('ac')]) == 1
assert count_task2_group([set('a'), set('a'), set('a'), set('a')]) == 1
assert count_task2_group([set('abcx'), set('abcy'), set('abcz')]) == 3
