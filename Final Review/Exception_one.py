def get_age():
    age = int(input())
    if age < 18 or age > 75: 
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age)*.7
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        calling = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {calling:.1f} bpm')
    except ValueError:
        print('Invalid age.\nCould not calculate heart rate info.')
