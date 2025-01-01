def jiffies_to_seconds(user_jiffies):
    number_seconds = user_jiffies*.01
    return number_seconds
    
if __name__ == '__main__':
    user_jiffies = float(input())
    number_seconds = jiffies_to_seconds(user_jiffies)
    print(f'{number_seconds:.3f}')
