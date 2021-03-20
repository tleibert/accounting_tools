#! /usr/bin/env python3
from collections import defaultdict

PROMPT = """Choose deprecation mode: Straight Line (sl),
Double-Declining Balance (dd), Activity Based (ab)
OR q to quit: """


def straight_line():
    start_value = int(input("Enter purchase price: "))
    end_value = int(input("Enter residual value: "))
    period = int(input("Enter service life: "))
    rate = (start_value - end_value) / period

    acc_dep = 0
    book_value = start_value
    for _ in range(period):
        dep_exp = rate
        acc_dep += rate
        book_value -= rate
        print(
            f"Dep. Expense: {dep_exp:0.0f}, Acc. Dep.: {acc_dep:0.0f}, Book Value: {book_value:0.0f}"
        )


def double_declining():
    start_value = int(input("Enter purchase price: "))
    end_value = int(input("Enter residual value: "))
    period = int(input("Enter service life: "))
    rate = 2 / period

    acc_dep = 0
    book_value = start_value
    for i in range(period):
        dep_exp = book_value * rate if i != period - 1 else book_value - end_value
        acc_dep += dep_exp
        book_value -= dep_exp
        print(
            f"Dep. Expense: {dep_exp:0.0f}, Acc. Dep.: {acc_dep:0.0f}, Book Value: {book_value:0.0f}"
        )


def activity_based():
    start_value = int(input("Enter purchase price: "))
    end_value = int(input("Enter residual value: "))
    total_hours = int(input("Enter total service hours: "))
    rate = (start_value - end_value) / total_hours
    usage = [
        int(ent) for ent in input("Enter usage by year(space separated): ").split()
    ]

    acc_dep = 0
    book_value = start_value
    for ent in usage:
        dep_exp = rate * ent
        acc_dep += dep_exp
        book_value -= dep_exp
        print(
            f"Dep. Expense: {dep_exp:0.0f}, Acc. Dep.: {acc_dep:0.0f}, Book Value: {book_value:0.0f}"
        )


FUNC_MAP = {
    "sl": straight_line,
    "dd": double_declining,
    "ab": activity_based,
}


def main():
    """
    Main function
    """
    call_table = defaultdict(lambda: lambda: print("Invalid choice!"), FUNC_MAP)
    call_table["q"] = exit
    try:
        while choice := input(PROMPT):
            try:
                call_table[choice]()
            except ValueError:
                print("Invalid number!")
    except EOFError:
        exit()


if __name__ == "__main__":
    main()
