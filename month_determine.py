#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines which month it is


def main():
    # This program determines which month it is
    # by getting an input form the user

    print("This program tells you the current month")
    print("")
    month_number = int(input("Please input the month number (1-12): "))
    print("")

    if month_number == 1:
        print("The 1st month is January")
    elif month_number == 2:
        print("The 2nd month is February")
    elif month_number == 3:
        print("The 3rd month is March")
    elif month_number == 4:
        print("The 4th month is April")
    elif month_number == 5:
        print("The 5h month is May")
    elif month_number == 6:
        print("The 6th month is June")
    elif month_number == 7:
        print("The 7th month is July")
    elif month_number == 8:
        print("The 8th month is August")
    elif month_number == 9:
        print("The 9th month is September")
    elif month_number == 10:
        print("The 10th month is October")
    elif month_number == 11:
        print("The 11th month is November")
    elif month_number == 12:
        print("The 12th month is December")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
