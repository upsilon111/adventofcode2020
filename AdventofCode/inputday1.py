f = open('/Users/syeds/Desktop/day1.txt', 'r')
expenses=list(map(str.strip, f.readlines()))
for i in range(0, len(expenses)):
    expenses[i] = int(expenses[i])
print(expenses)
