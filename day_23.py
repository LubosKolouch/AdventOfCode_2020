#!/bin/env python
""" Advent of Code Day 23 """


class Cup:
    """ Class holding each cup """
    def __init__(self, cup_id: int):
        self.cup_id = cup_id
        self.next_cup = None

    def __str__(self):
        return f"Cup {self.cup_id}, next {self.next_cup}"


class Day23:
    """ Class for processing of day 23 """
    def __init__(self, cups: str, task: int = 1) -> None:

        self.cups_orig = cups
        self.cups_dict = {}
        self.task = task
        for cup_nr, cup in enumerate(cups):
            cups_obj = Cup(int(cup))

            if cup_nr != len(cups) - 1:
                cups_obj.next_cup = int(cups[cup_nr + 1])
            else:
                cups_obj.next_cup = int(cups[0])

            self.cups_dict[int(cup)] = cups_obj
            self.cups_count = 9

        if task == 2:
            current_cup = int(self.cups_orig[-1])

            for i in range(10, 1000001):
                new_cup = Cup(i)
                self.cups_dict[current_cup].next_cup = i

                self.cups_dict[i] = new_cup
                current_cup = i

            self.cups_dict[1000000].next_cup = int(self.cups_orig[0])

            self.cups_count = 1000000

    def get_task(self, rounds: int):
        """ Count the solution for task 1"""

        current_cup = int(self.cups_orig[0])

        for _ in range(rounds):
            picked_up = []
            moving_item = current_cup
            for _ in range(3):
                moving_item = self.cups_dict[moving_item].next_cup
                picked_up.append(moving_item)

            next_item = self.cups_dict[moving_item].next_cup
            self.cups_dict[current_cup].next_cup = next_item

            destination_cup = current_cup - 1 if current_cup > 1 else self.cups_count

            while destination_cup in picked_up:
                destination_cup = destination_cup - 1 if destination_cup > 1 else self.cups_count

            self.cups_dict[picked_up[-1]].next_cup = self.cups_dict[
                destination_cup].next_cup
            self.cups_dict[destination_cup].next_cup = picked_up[0]

            current_cup = self.cups_dict[current_cup].next_cup

        result = ''

        if self.task == 1:
            current_cup = self.cups_dict[1].next_cup
            while self.cups_dict[current_cup].cup_id != 1:
                result += str(self.cups_dict[current_cup].cup_id)
                current_cup = self.cups_dict[current_cup].next_cup

            print(f"Task1: {result}")
            return int(result)

        id1 = self.cups_dict[1].next_cup
        id2 = self.cups_dict[id1].next_cup

        print(f"Task2: {int(id1)*int(id2)}")
        return int(id1) * int(id2)


def test_app():
    """ Run the tests """
    test1 = Day23('389125467')
    assert test1.get_task(10) == 92658374
    test2 = Day23('389125467')
    assert test2.get_task(100) == 67384529


def test_task2():
    """ Test the Part 2 """
    test3 = Day23('389125467', task=2)
    assert test3.get_task(10000000) == 149245887792


if __name__ == "__main__":
    day_processor = Day23('362981754')
    day_processor.get_task(100)

    day_processor = Day23('362981754', task=2)
    day_processor.get_task(10000000)
