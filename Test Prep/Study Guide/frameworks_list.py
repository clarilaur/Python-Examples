frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
    index = int(input())
    locate = frameworks[index]
    print(locate)

except:
    print('Error')
