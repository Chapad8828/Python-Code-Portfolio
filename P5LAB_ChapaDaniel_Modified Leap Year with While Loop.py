# Define your function here.


def days_in_feb(user_year):
    if (user_year % 4 == 0):
        if (user_year % 100 == 0):
            if (user_year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

while True:
    user_input = input("Enter a year to test or enter 'done' to exit: ")
    if user_input.lower() == 'done':
        break
    else:
        try:
            year = int(user_input)
            if days_in_feb(year) == 29:
                print(year, "has 29 days in February.")
            else:
                print(year, "has 28 days in February.")
        except ValueError:
            print("Invalid input. Please enter a valid year or 'done' to exit.")
