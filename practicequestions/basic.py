# Student Management Mini Program

print("===== STUDENT MANAGEMENT =====")

# Input + Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# List
subjects = ["Python", "Maths", "Physics", "Chemistry"]

print("\nYour subjects:")
for i in range(len(subjects)):
    print(i + 1, subjects[i])

# Indexing
print("\nFirst subject:", subjects[0])
print("Last subject:", subjects[-1])

# Marks
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Function
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


# Function call
average = calculate_average(marks)

# If / Elif / Else
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

# Dictionary
student = {
    "name": name,
    "age": age,
    "marks": marks,
    "average": average,
    "grade": grade
}

# While loop
print("\n===== RESULT =====")

count = 0

while count < len(subjects):
    print(subjects[count], ":", marks[count])
    count += 1

# String methods
print("\nName in uppercase:", name.upper())
print("Name in lowercase:", name.lower())

# Operators
total_marks = sum(marks)
percentage = total_marks / len(marks)

print("\nTotal Marks:", total_marks)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)

# Comparison + Logical operators
if age >= 18 and average >= 60:
    print("You are eligible and performing well.")
elif age >= 18:
    print("You are eligible, but improve your marks.")
else:
    print("Keep learning and improving!")

print("\nStudent Details:")
print(student)

print("\n===== PROGRAM END =====")