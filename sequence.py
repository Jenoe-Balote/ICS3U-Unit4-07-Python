#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: May 2021
# This program prints all numbers 1000 to 2000
#   with five numbers printed each line


def main():
    # This function prints the number values in range

    # process & output
    for loop_sequence in range(1000, 2000 + 1):
        if loop_sequence % 5 == 4:
            print("{} ".format(loop_sequence))
        else:
            print("{} ".format(loop_sequence), end="")
    print("\nAll done!")


if __name__ == "__main__":
    main()
