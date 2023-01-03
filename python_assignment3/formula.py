# 12. Write a program to add first seven terms of the following series using a for loop
# 1/1! + 2/2! + 3/3! + ... + n/n!


sum = 0
for i in range(1,10):
    fact = 1
    for j in range(1,i+1):
        fact*=j
    sum += int(i/fact)

print(sum)


