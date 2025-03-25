import numpy as np

# Generate Random Student Marks
np.random.seed(42)  # For reproducibility
marks = np.random.randint(50, 100, (5, 3))  # 5 students, 3 subjects
subjects = ["Math", "Science", "English"]

print("Student Marks:\n", marks)

# Calculate Average Marks for Each Student
average_marks = np.mean(marks, axis=1)
print("\nAverage Marks of Each Student:", average_marks)

# Find Highest and Lowest Marks in Each Subject
highest_marks = np.max(marks, axis=0)
lowest_marks = np.min(marks, axis=0)

print("\nHighest Marks in Each Subject:", dict(zip(subjects, highest_marks)))
print("Lowest Marks in Each Subject:", dict(zip(subjects, lowest_marks)))

# Compute Overall Class Average
class_average = np.mean(marks)
print("\nClass Average:", class_average)

# Determine the Top-Performing Student
top_student = np.argmax(average_marks) + 1  # +1 to match student numbering
print("\nTop-Performing Student: Student", top_student)
