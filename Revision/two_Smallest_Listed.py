split = list(map(int, input().split()))

small1 = min(split)
    
split.remove(small1)

small2 = min(split)

print(f'{small1} and {small2}')
