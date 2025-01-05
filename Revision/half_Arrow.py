arrowbaseheight = int(input()) 
width = int(input())   

headwidth = int(input())
while headwidth <= width:  
    headwidth = int(input())  

for i in range(1, arrowbaseheight + 1):
    print('*' * width)

for i in range(headwidth, 0, -1):
    print('*' * i)
