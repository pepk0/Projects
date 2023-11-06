def get_float_input(prompt: str) -> float:
    while True:
        try:
            float_input = float(input(prompt))
            if float_input.is_integer():  # type: ignore
                float_input = int(float_input)
            return float_input
        except ValueError:
            print("invalid number")


def get_choice(prompt: str) -> str:
    valid_choices = ("1", "2", "3", "4", "5",)
    while True:
        try:
            user_choice = input(prompt)
            if user_choice not in valid_choices:
                raise ValueError
            return user_choice
        except ValueError:
            print("Invalid option,choice must be 1, 2, 3, 4 or 5!")


def addition(num_one, num_two) -> str:
    result = round(num_one + num_two, 2)
    return f"Result: {num_one} + {num_two} = {result}"


def subtraction(num_one, num_two) -> str:
    result = round(num_one - num_two, 2)
    return f"Result: {num_one} - {num_two} = {result}"


def division(num_one, num_two) -> str | bool:
    try:
        result = round(num_one / num_two, 2)
        return f"Result: {num_one} / {num_two} = {result}"
    except ZeroDivisionError:
        return False


def multiplication(num_one, num_two) -> str:
    result = round(num_one * num_two)
    return f"Result: {num_one} * {num_two} = {result}"


def main():
    print("Menu:\n", " 1.Addition", " 2.Subtraction", " 3.Multiplication",
          " 4.Division", " 5.Quit", sep="\n")

    while True:
        choice = get_choice("\nEnter your choice (1/2/3/4/5): ")
        if choice == "5":
            print("Goodbye!")
            return

        result = None
        first_number = get_float_input("Enter the first number: ")
        second_number = get_float_input("Enter the second number: ")
        if choice == "1":
            result = addition(first_number, second_number)
        elif choice == "2":
            result = subtraction(first_number, second_number)
        elif choice == "3":
            result = multiplication(first_number, second_number)
        elif choice == "4":
            result = division(first_number, second_number)
            if not result:
                result = "Can't divide by zero!"

        print(result)


if __name__ == "__main__":
    main()
