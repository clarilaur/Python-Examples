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

if student_grades['Pippy'] <= 70:
    print('Keep going pipper-chino you got this!')
else:
    print('You did it baby!')

for student in student_grades:
    print('{}, you earned {} on the final exam'.format(student, student_grades[student]))
