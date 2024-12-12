import csv

# Read a CSV file
with open('student_grades.csv', 'r') as f:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        
# Write a CSV file
with open('student_grades.csv', 'w', newline='') as f:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age'])  # header row
    writer.writerow(['John', 25])
    writer.writerow(['Jane', 30])
    
#extra helpful tips:
contents = f.read() #whole file as one big string
contents = f.readlines() #a list of line by line strings, WILL have \n at the end of each string

#MEMORIZE THIS:
contents =list(csv.reader()) #csv.reader-makes a list of lists instead of the list of strings we get from readlines()
