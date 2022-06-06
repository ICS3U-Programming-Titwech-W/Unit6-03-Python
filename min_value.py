#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.30.2022
# program genertate numbers, puts them
# into a list then displays it

import constants
import random


def min_value(rand_num):

    min = rand_num[0]

    # calculate the max value
    for counter in range(len(rand_num)):
        if min > rand_num[counter]:
            min = rand_num[counter]
    return min


def main():

    # initlizing sum and counter
    counter = 0
    sum = 0

    # declaring empty list
    list_of_num = []

    for counter in range(constants.MAX_SIZE):
        list_of_num.append(random.randint
                           (constants.MIN_NUM, constants.MAX_NUM))

        sum = sum + list_of_num[counter]
        print("{} is added to the list at position {}"
              . format(list_of_num[counter], counter))

    min_user = min_value(list_of_num)
    print("")
    print("The max value is: {}" .format(min_user))


if __name__ == "__main__":
    main()
