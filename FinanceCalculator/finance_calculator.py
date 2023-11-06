def get_num(prompt: str, scope=None, error="number") -> float:
    """"loops until a valid int or float are given, 
    space controls the range of the number
    error prints the expected type of input when not given"""
    while True:
        try:
            number = float(input(prompt))
            if scope:
                lower_range, upper_range = scope
                if number < lower_range or number > upper_range:
                    raise ValueError
            return number
        except ValueError:
            print(f"Invalid {error}")


def calc_simple_interest() -> str:
    principal_amount = get_num("Enter principal amount: ")
    interest_rate = get_num(
        "Enter annual interest rate %: ", (1, 100), "percent")
    time = get_num("Enter time (in years): ")
    # converting to decimal percent
    interest_rate /= 100
    result = principal_amount * (1 + interest_rate * time)
    result -= principal_amount
    return f"\nSimple interest ${result:,.2f}\n"


def calc_compound_interest() -> str:
    principal_amount = get_num("Enter principal amount: ")
    interest_rate = get_num(
        "Enter annual interest rate %: ", (1, 100), "percent")
    time = get_num("Enter time (in years): ")
    compound_per_year = get_num(
        "Enter the number of times interest is compounded per year: ",
        (1, 12))
    # converting to decimal percent
    interest_rate /= 100
    result = (principal_amount * (1 + (interest_rate / compound_per_year))
              ** (compound_per_year * time))
    result -= principal_amount
    return f"\nCompound Interest: ${result:,.2f}\n"


def calc_loan_payment() -> str:
    loan_amount = get_num("Enter loan amount: ")
    interest_rate = get_num("Enter interest rate %: ", (1, 100), "percent")
    number_mounts = get_num("Enter number mounts: ")
    # converting to decimal percent
    interest_rate /= 100
    result = (loan_amount * (interest_rate / 12) * (1 + interest_rate / 12)
              ** number_mounts)
    result /= (1 + interest_rate / 12) ** number_mounts - 1
    return f"\nMonthly Payment: ${result:,.2f}\n"


def calc_future_value() -> str:
    investment_amount = get_num("Enter investment amount: ")
    interest_rate = get_num("Enter interest rate %: ", (1, 100), "percent")
    number_years = get_num("Enter number of years: ")
    # converting to decimal percent
    interest_rate /= 100
    result = investment_amount * (1 + interest_rate) ** number_years
    return f"\nFuture value: ${result:,.2f}\n"


def user_quit(prompt: str,) -> bool:
    valid_choices = ("yes", "no")
    while True:
        user_choice = input(prompt)
        if user_choice in valid_choices:
            if user_choice == "yes":
                return False
            else:
                return True
        else:
            print(f"choice must be {valid_choices}!")


def main():
    # bool flag
    calc_running = True

    while calc_running:
        # Main Menu of choices
        print("Main Menu:\n", " 1.Calculate Simple Interest",
              " 2.Calculate Compound Interest", " 3.Calculate Loan Payment",
              " 4.Calculate Future Value of Savings", " 5.Quit", sep="\n")

        to_print = ""
        user_choice = get_num(
            "\nEnter your choice (1/2/3/4/5): ", (1, 5), "choice")

        if user_choice == 1:
            print("\nCalculate Simple Interest\n")
            to_print = calc_simple_interest()
        elif user_choice == 2:
            print("\nCalculate Compound Interest\n")
            to_print = calc_compound_interest()
        elif user_choice == 3:
            print("\nCalculate Loan Payment\n")
            to_print = calc_loan_payment()
        elif user_choice == 4:
            print("\nCalculate Future Value of Savings\n")
            to_print = calc_future_value()
        else:
            calc_running = False
            continue

        print(to_print)

        if user_quit("Do you want to perform another calculation?: "):
            calc_running = False
            continue

    else:
        (print("\nGoodbye!\n"))  # if flag is false we execute this


if __name__ == "__main__":
    main()
