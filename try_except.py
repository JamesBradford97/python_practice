try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as errOr:
    print(errOr)
except ValueError:
    print("Invalid Input")