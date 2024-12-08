#Track laps to miles

def laps_to_miles(user_laps):
    number_of_miles = float(user_laps) * 0.25
    return number_of_miles

if __name__ == '__main__':
    try:
        user_laps = float(input())
        print(f'{laps_to_miles(user_laps):.2f}')
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
