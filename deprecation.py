#! /usr/bin/env python3

PROMPT = """Choose deprecation mode: Straight Line (sl),
Double-Declining Balance (dd), Activity Based (ab)
OR q to quit: """


def straight_line():
    """
    Prompts for and calculates deprecation using the straight-line
    method.

    Raises
    ======
    ValueError if invalid input is supplied
    """
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
    """
    Prompts for and calculates deprecation using the double-declining
    balance method.

    Raises
    ======
    ValueError if invalid input is supplied
    """
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
    """
    Prompts for and calculates deprecation using the activity-based
    method. (Also known as units-of-production)

    Raises
    ======
    ValueError if invalid input is supplied
    """
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
    "q": exit,
}


def main():
    """
    Main function
    """


while True:
    try:
        FUNC_MAP[input(PROMPT)]()
    except KeyError:
        print("Invalid choice!")
    except ValueError:
        print("Invalid number!")
    except EOFError:
        break

if __name__ == "__main__":
    main()
