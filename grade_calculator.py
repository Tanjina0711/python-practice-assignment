
# Student Grade Calculator

name = input("Enter student name: ")
print()

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

# Check if marks are valid
if not (0 <= math <= 100 and 0 <= english <= 100 and 0 <= python_marks <= 100):
    print("\nInvalid marks! Each subject mark must be between 0 and 100.")

else:
    # Calculate average
    average = (math + english + python_marks) / 3

    # Determine grade
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Display result
    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
