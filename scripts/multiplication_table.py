#!/usr/bin/env python3
"""
Multiplication Table Program

This script prompts the user to enter a number and prints its multiplication table from 1 to 10.
"""

def main():
    try:
        number = int(input("Enter a number to generate its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print(f"\nMultiplication table for {number}:\n")
    for i in range(1, 11):
        result = number * i
        print(f"{number} × {i} = {result}")

if __name__ == "__main__":
    main()
