# Open the file and read line by line
with open('/Users/lauraarnold/PycharmProjects/PythonProject/student_grades.py', 'r') as file:
    my_lines = []  # List to store stripped lines
    for line in file:
        # Print a message for each line
        print('Hey pups!')
        # Append the stripped line to the list
        my_lines.append(line.strip())

# Print the list of stripped lines
print("Lines from the file:")
print(my_lines)
