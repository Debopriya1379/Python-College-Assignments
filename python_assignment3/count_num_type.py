# Write a program to enter the numbers till the user wants and at the end it should display the
# count of positive, negative and zeros entered.

n = int(input('Enter number of inputs you want to give'))

count_of_positive = 0
count_of_negative = 0
count_of_zero = 0

for i in range(n):
    ele = int(input())
    if ele>0 :
        count_of_positive+=1
    elif ele<0 :
        count_of_negative+=1
    else :
        count_of_zero+=1

print("count of positive numbers : ", count_of_positive)
print("count of negative numbers : ", count_of_negative)
print("count of zeros : ", count_of_zero)