# Reading the file
with open('/Users/lauraarnold/PycharmProjects/PythonProject/student_grades.py', 'r') as f1:
    content = f1.read()
    f1.readlines() #returns a list of strings/this is out of place


    print(content)

# Overwriting the file
with open('/Users/lauraarnold/PycharmProjects/PythonProject/student_grades.py', 'w') as f1:
    f1.write('This is overwriting the content I had before about the pups.\n')
    f1.close() #closes a file
