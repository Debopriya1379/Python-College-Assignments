# Write a program to find the range of a set of numbers. Range is the difference between the
# smallest and biggest number in the list.

n = int(input('Enter no. of inputs'))
max_num = -99999999999
min_num = 10000000000

print('Enter inputs')
for i in range(n):
    ele = int(input())
    if ele>max_num:
        max_num = ele
    if ele<min_num:
        min_num = ele

calculated_range = max_num-min_num
print(calculated_range)