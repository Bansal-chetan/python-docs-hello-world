#!/usr/bin/env python3
"""Simple interactive CLI calculator.

Features:
- add, subtract, multiply, divide
- power, modulus, square root, factorial
- view and clear history
"""
import math
import sys


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer, please try again.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)


def show_menu():
    print("\nSimple Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Power (a^b)")
    print("6) Modulus")
    print("7) Square root")
    print("8) Factorial (integer)")
    print("9) View history")
    print("10) Clear history")
    print("0) Exit")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                a = get_number("First number: ")
                b = get_number("Second number: ")
                res = add(a, b)
                print("Result:", res)
                history.append(f"{a} + {b} = {res}")

            elif choice == "2":
                a = get_number("First number: ")
                b = get_number("Second number: ")
                res = subtract(a, b)
                print("Result:", res)
                history.append(f"{a} - {b} = {res}")

            elif choice == "3":
                a = get_number("First number: ")
                b = get_number("Second number: ")
                res = multiply(a, b)
                print("Result:", res)
                history.append(f"{a} * {b} = {res}")

            elif choice == "4":
                a = get_number("Dividend: ")
                b = get_number("Divisor: ")
                res = divide(a, b)
                print("Result:", res)
                history.append(f"{a} / {b} = {res}")

            elif choice == "5":
                a = get_number("Base: ")
                b = get_number("Exponent: ")
                res = power(a, b)
                print("Result:", res)
                history.append(f"{a} ^ {b} = {res}")

            elif choice == "6":
                a = get_number("First number: ")
                b = get_number("Second number: ")
                res = modulus(a, b)
                print("Result:", res)
                history.append(f"{a} % {b} = {res}")

            elif choice == "7":
                a = get_number("Number: ")
                res = square_root(a)
                print("Result:", res)
                history.append(f"sqrt({a}) = {res}")

            elif choice == "8":
                n = get_int("Integer: ")
                res = factorial(n)
                print("Result:", res)
                history.append(f"{n}! = {res}")

            elif choice == "9":
                if not history:
                    print("No history yet.")
                else:
                    print("History:")
                    for i, item in enumerate(history, 1):
                        print(f"{i}: {item}")

            elif choice == "10":
                history.clear()
                print("History cleared.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice, please enter a number from the menu.")

        except ZeroDivisionError as e:
            print("Error:", e)
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
