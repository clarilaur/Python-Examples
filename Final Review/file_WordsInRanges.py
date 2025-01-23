def main():
    
    input_filename = input() 
    lower_bound = input() 
    upper_bound = input()  
    
    with open(input_filename, 'r') as file:
        lines = file.readlines() 

    # Step 3: Process each line and check if it's within the bounds
    for line in lines:
        line = line.strip()  # 
        if lower_bound <= line <= upper_bound:
            print(line)  # 


if __name__ == "__main__":
    main()
