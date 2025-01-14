try:
    integers = []  
    counter = 0 
    
    for _ in range(3):  
        num = int(input())
        integers.append(num)
        counter += 1

    
    print(max(integers))

except EOFError:
    if counter == 0:
        print("0 input(s) read:\nNo max")  
    else:
        print(f"{counter} input(s) read:\nMax is {max(integers)}")
