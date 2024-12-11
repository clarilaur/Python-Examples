student_grades = {
    'Rio': 99,
    'Pippy': 69,
    'Clari': 100
}

for student in student_grades:
    print('Nice effort')
if 'Pippy' in student_grades:
    print(student_grades.get('Clari'))
    print(student_grades.get('Pippy'))
    print(student_grades.get('Rio'))

while 'Pippy' <= str(70):
    print('Keep going pipper-chino you got this!')
print('You did it baby!')
