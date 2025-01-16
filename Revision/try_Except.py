frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try: 
    index = int(input())
    indexvalue = frameworks[index]
    print(indexvalue)
    
except:
    print('Error')
