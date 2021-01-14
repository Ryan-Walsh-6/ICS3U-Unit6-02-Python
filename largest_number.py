#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program picks out the largest number out of 10 random numbers

import random


def largest_number(list_of_numbers):
    # calculates volume

    # process & output
    for loop_counter in range(1, len(list_of_numbers)):
        if list_of_numbers[0] < list_of_numbers[loop_counter]:
            list_of_numbers[0] = list_of_numbers[loop_counter]

    return list_of_numbers[0]


def main():
    # this program picks out the largest number out of 10 random numbers
    my_numbers = []
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)

    for loop_counter in range(0, 10):
        print("The random number {0} is: {1}".format(loop_counter + 1,
                                                     my_numbers[loop_counter]))

    big_numb = largest_number(my_numbers)

    print("\n", end="")
    print("The largest number is {0}".format(big_numb))


if __name__ == "__main__":
    main()
