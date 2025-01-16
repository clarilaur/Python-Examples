a = 15.62
b = 41.85
c = 32.67

atrip = int(input())
btrip = int(input())
ctrip = int(input())

total_miles_traveled = (a*atrip)+(b*btrip)+(c*ctrip)
#solution outputs "Distance: " followed by the total value to two decimal places
print(f'Distance: {total_miles_traveled:.2f} miles')
