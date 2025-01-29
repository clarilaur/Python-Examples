input_filename = 'students.txt'
group = {}
with open(input_filename, 'r') as f:
    lines = f.readlines()
    for i in range(0,len(lines),2):
        s_name = [i].strip()
        s_grade = int([i+1].strip())
    if s_grade not in group:
        group[s_grade] = [s_name]  # Create new list if grade not in dictionary
    else:
        group[s_grade].append(s_name)
with open('grades_groups.txt', 'w') as file:
    for grade in sorted(group.keys()):  # Sort by grade
        names = '; '.join(group[grade])  # Convert list to a string
        file.write(f"{grade}: {names}\n")  # Write to file

with open('students_sorted.txt', 'w') as file:
    all_students = []
    for students in group.values():  # Collect all student names
        all_students.extend(students)

    for student in sorted(all_students):  # Sort names alphabetically
        file.write(f"{student}\n")  # Write each name to file
