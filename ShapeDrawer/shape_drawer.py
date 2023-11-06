def get_int(prompt: str) -> int:
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("invalid int")


def get_valid_direction(prompt: str, directions: str) -> str:
    valid_directions = directions

    while True:
        direction = input(prompt)
        if direction in valid_directions:
            return direction
        print("invalid directions")


def draw_triangle() -> None:
    print()
    height = get_int("Enter the number of rows for the triangle: ")
    direction = get_valid_direction("Enter 'u' for upward \
                                    or 'd' for downward: ", "du")

    triangle_height = range(1, height + 1)

    if direction == "d":
        triangle_height = triangle_height[::-1]

    print()
    for i in triangle_height:
        print(f"{'*' * i}")


def draw_rectangle() -> None:
    print()
    rows = get_int("Enter the number of rows for the rectangle: ")
    columns = get_int("Enter the number of columns for the rectangle: ")

    print()
    for _ in range(rows):
        print("*" * columns)


def draw_pyramid() -> None:
    print()
    rows = get_int("Enter the number of rows for the pyramid: ")
    columns = rows * 2 - 1

    print()
    stars = 1
    for _ in range(rows):
        extra_space = (" " * ((columns - stars) // 2))
        print(extra_space + ("*" * stars) + extra_space)
        stars += 2


menu = ("Menu:\n1. Draw a Triangle\n"
        "2. Draw a Rectangle\n3. Draw a Pyramid\n4. Quit")
print(menu)

while True:

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "4":
        print("\nGoodbye!\n")
        break

    elif choice == "1":
        draw_triangle()

    elif choice == "2":
        draw_rectangle()

    elif choice == "3":
        draw_pyramid()

    else:
        print("\ninvalid choice")
