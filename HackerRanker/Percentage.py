# A dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided,
# showing 2 places after the decimal.

student_marks = {"A":[20,30,40],"B":[52,56,60]}
queryname = "A"

# Average of all students:

for i in student_marks:
    scores = student_marks[i]
    average = sum(scores)/len(scores)
    print(format(average, ".2f"))                   # Formats to 2 decimal places

# Average of specific student:

if queryname in student_marks:
    scores = student_marks[queryname]
    average = sum(scores)/len(scores)
print(format(average, ".2f"))



