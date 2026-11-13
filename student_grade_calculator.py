name = input("Enter student name: ")

math_marks = float(input("Enter Math marks: "))
english_marks = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

total_marks = math_marks + english_marks + python_marks
average = total_marks / 3

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks:g}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")