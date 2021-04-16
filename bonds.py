PROMPT = """Calculate (i)ssue price,
(a)mortization schedule, or (b)oth: """

AMORTIZER_LOOP_STRING = (
    "Payment no. {}, Cash Interest Payment: {:.2f},"
    " Interest Expense: {:.2f}, Amortizement: {:.2f}, Carrying Value: {:.2f}"
)

AMORTIZER_FINAL_STRING = (
    "TOTAL: Interest Paid: {:.2f}, Interest Expense: {:.2f}, Amortization: {:.2f}\n"
)


def pva(i, n):
    """ Calculates the present value of an annuity of $1 """
    return (1 - 1 / ((1 + i) ** n)) / i


def pv(i, n):
    """ Calculates the present value of $1 """
    return 1 / (1 + i) ** n


def amortizer(carrying_value, interest_payment, market_rate, num_years, periods):
    print(f"START: Carrying Value: {carrying_value:.2f}")
    total_paid = 0
    total_expense = 0
    total_amortized = 0

    for i in range(periods * num_years):
        interest_expense = carrying_value * market_rate / periods
        amortize_amount = interest_expense - interest_payment
        carrying_value += amortize_amount
        print(
            AMORTIZER_LOOP_STRING.format(
                i,
                interest_payment,
                interest_expense,
                abs(amortize_amount),
                carrying_value,
            )
        )

        total_paid += interest_payment
        total_expense += interest_expense
        total_amortized += amortize_amount

    print(
        AMORTIZER_FINAL_STRING.format(total_paid, total_expense, abs(total_amortized))
    )


def issue_price():
    """
    Calculates the issue price of a bond

    Returns:
    - face value of bond
    - carrying value of bond
    - market rate of bond
    - interest payment on bond
    """
    face_value = float(input("Enter bond face value: "))
    stated_rate = float(input("Enter stated/face rate: ")) / 100
    market_rate = float(input("Enter market interest rate: ")) / 100
    years = int(input("Enter number of years: "))
    periods_per_year = int(
        i if (i := input("Enter number of periods per year (default 2): ")) != "" else 2
    )

    payment = face_value * stated_rate / periods_per_year
    payment_value = payment * pva(
        market_rate / periods_per_year, years * periods_per_year
    )
    bond_value = face_value * pv(
        market_rate / periods_per_year, years * periods_per_year
    )
    bond_value += payment_value

    print(f"The bond of ${face_value} issues at a value of ${bond_value:.2f}\n")
    return bond_value, payment, market_rate, years, periods_per_year


def amortize():
    face_value = float(input("Enter bond face value: "))
    sale_price = float(input("Enter bond sale price: "))
    stated_rate = float(input("Enter stated/face rate: ")) / 100
    market_rate = float(input("Enter market interest rate: ")) / 100
    years = int(input("Enter number of years: "))
    periods_per_year = int(
        i if (i := input("Enter number of periods per year (default 2): ")) != "" else 2
    )

    payment = face_value * stated_rate / periods_per_year
    amortizer(sale_price, payment, market_rate, years, periods_per_year)


def issue_and_amortize():
    amortizer(*issue_price())


FUNC_MAP = {"i": issue_price, "a": amortize, "b": issue_and_amortize, "q": exit}


def main():
    """ Prompts user for input """
    try:
        while choice := input(PROMPT):
            try:
                FUNC_MAP.get(choice, lambda: print("Invlaid Choice"))()
            except ValueError:
                print("Invalid number!")
    except EOFError:
        exit()


if __name__ == "__main__":
    main()
