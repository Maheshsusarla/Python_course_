
Task 1
number=int(input("Enter the number "))
if number >=0:
    print("Positive")
else:
    print("Negative")

problem 2
a=int(input("Enter the first number "))
b=int(input("Enter the first number "))
if a>b:
    print(f"Large number{a}")
elif b>a:
    print(f"Large number {b}")
else:
    print("High number")

problem3
year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")