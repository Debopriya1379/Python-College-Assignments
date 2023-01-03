# i=0
# check=0
# while(i<=30):
#     j = str(i)
#     for k in range(len(j)):
#         check+=int(j[k])**3
#     if(i==check):
#         print(i)
#         check=0
#     check=0


# x = int(input("Enter Number"))
# temp = x
# sum=0

# while(temp>0):
#     digit = (temp%10)
#     sum = sum + (digit**3)
#     temp = temp//10

# if(x==sum):
#     print("Armstrong number")
# else :
#     print("Not a Armstrong number")


print("Armstrong numbers between 1 to 500")
for i in range(1,501):
    order = len(str(i))
    temp = i
    sum = 0
    while(temp>0):
        digit = (temp%10)
        sum += (digit**order)
        temp //= 10
    if(i == sum):
        print(i," ",end='')