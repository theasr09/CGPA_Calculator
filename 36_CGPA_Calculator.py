# Define the grade scale and corresponding grade points
grade_scale = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

# Function to calculate CGPA
def calculate_cgpa(grades):
    total_grade_points = sum(grade_scale.get(grade, 0) for grade in grades)
    cgpa = total_grade_points / len(grades)
    return cgpa

# Input: Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Input: Grades for each subject
grades = []
for i in range(num_subjects):
    grade = input(f"Enter the grade for subject {i+1}: ").upper()
    grades.append(grade)

# Calculate CGPA
cgpa = calculate_cgpa(grades)

# Display CGPA
print(f"Your CGPA is: {cgpa:.2f}")