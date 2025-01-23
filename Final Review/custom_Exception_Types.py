class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  


def find_ID(name, info):
    if name in info:
        return info[name]
    else: 
        raise StudentInfoError(f'Student ID not found for {name}')
    
    
def find_name(ID, info):
    reversed_info = {v: k for k, v in info.items()}
    if ID in reversed_info:
        return reversed_info[ID]
    else: 
        raise StudentInfoError(f"Student name not found for {ID}")

if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input()    
    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
            print(result)
        else:
            ID = input()
            result = find_name(ID, student_info)
            print(result)
    except StudentInfoError as e:
        print(e.message)
