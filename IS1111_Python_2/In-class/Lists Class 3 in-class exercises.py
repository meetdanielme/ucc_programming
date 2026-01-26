# Row: [Student, Grade, Age]
# Note: There are NO headers here. Just data.

from operator import index


students = [
    ["Alice", 90, 20], 
    ["Bob", 45, 22], 
    ["Charlie", 100, 19]
]
# How many items/rows are in the main list?
print(len(students))
# How do I access the entire list for "Bob"?
print(students[1])
# (2D Indexing) How do I get JUST Bob's Grade (45)?
# Syntax: list[row][col]
print(students[1][1])
# The teacher made a mistake. Bob actually got 50. Change it.
students[1][1] = 50
# We want to find the Class Average. 
# But we can't run sum() on the 2D list. We need a flat list of just numbers.

scores = []

# Loop through 'students', extract the score (index 1), and append to 'scores'.

for student in students:
    scores.append(student[1])

# for /in 

print(f"Flat Scores List: {scores}")

# How do I get the total sum of all scores?

total_score = sum(scores)
print(f"Total Score: {total_score}")

# What is the highest score?

print(f"Highest Score: {max(scores)}")  

# What is the lowest score?

print(f"Lowest Score: {min(scores)}")

# How do I calculate the Average Score?

print(f"Average Score: {total_score / len(scores)}")

# We know the highest score is 100. But WHO got it? (for in/ index)

highest_grade = ''
maximum_grade = max(scores)
for student in students:
    if student[1] == maximum_grade:
        highest_grade_index = scores.index(maximum_grade) # index returns the position of the first occurrence of a specified value
        highest_grade_name = students[highest_grade_index][0]
        print(f"Highest Grade: {highest_grade_name} with a score of {maximum_grade}")

# Real data usually comes with labels (Headers).
raw_data = [
    ["Name", "Score", "Age"],    # Index 0 is a Header!
    ["Alice", 90, 20], 
    ["Bob", 50, 22], 
    ["Charlie", 100, 19]
]

# What happens if I try to calculate the sum of column 2 now?

for row in raw_data:
    print(row[1])  # This will print the header "Score" as well!


# Create a variable 'clean_data' that removes the Header row.

clean_data = raw_data[1:]

# Prove it worked. Print the length of raw_data vs clean_data.

print(f"Length of raw_data: {len(raw_data)}")
print(f"Length of clean_data: {len(clean_data)}")

# Now we can re-run our logic from Part 2 on 'clean_data'.

scores = []
for student in clean_data:
    scores.append(student[1])