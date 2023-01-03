# m = int(input("Entera number"))
# n = oct(m)
# print("It's octal equivalent is : ", n)

n = int(input("Enter a number "))
octalNum = [0] * n

i = 0
while (n != 0):
    octalNum[i] = n % 8
    n = int(n / 8)
    i += 1

for j in range(i - 1, -1, -1):
    print(octalNum[j], end="")
    
print()