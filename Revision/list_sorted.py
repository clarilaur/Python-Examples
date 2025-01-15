numbers = list(map(int, input().split()))

start, end = map(int, input().split())

start -= 1
end -= 1

if numbers[start:end+1] == sorted(numbers[start:end+1]):
    print("yes")
else:
    print("no")
