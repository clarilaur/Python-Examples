data = list(map(int,input().split()))

n = int(input().strip())

lengthn = abs(n)

if len(data) >= lengthn:
        index = data[n]
        print(index)
else:
        print(n)
