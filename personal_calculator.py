
# Personal Calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"\nHello, {name}!")
print(f"Your age is {age}.\n\n")


print(f"Addition: {addition:g}")
print(f"Subtraction: {subtraction:g}")
print(f"Multiplication: {multiplication:g}")

if second_number != 0:
    division = first_number / second_number
    print(f"Division: {division:2f}")
else:
    print("Division: Undefined (cannot divide by zero)")
