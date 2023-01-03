# 1. Program to declare and print a list.

# new_list = [3, 6, 9, 21, 4, 76]
# print(new_list)

###################################################

# 2. Python program to print list elements in different ways.

# new_list = [3, 6, 9, 21, 4, 76]
# print(new_list)

# for i in range(len(new_list)) :
#     print(new_list[i],' ', end='')

# for i in new_list :
#     print( i ,' ', end='')

###################################################

# 3. Program for Adding, removing elements in the list.

# new_list = [3, 6, 9, 21, 4, 76]
# new_list.append(99)
# new_list.remove(6)
# print(new_list)

###################################################

# 4. Program to print a list using 'FOR and IN' loop.

# new_list = [3, 6, 9, 21, 4, 76]
# for i in new_list :
#     print( i,' ', end='')

###################################################

# 5. Program to add an element at specified index in a list.

# new_list = [3, 6, 9, 21, 4, 76]
# new_list.insert(1,99)   #in serting 99 at index 1
# print(new_list)

################################################### 

# 6. Program to remove first occurrence of a given element in the list.

# new_list = [3, 6, 9, 2, 3, 4, 6]
# print('before')
# print(new_list)
# r_ele = 6
# for i in new_list[:] :
#    if(i==r_ele) :
#     new_list.remove(i)
#     break
# print('after')
# print(new_list)

###################################################

# 7. Remove all occurrences a given element from the list.

# new_list = [3, 6, 9, 2, 3, 4, 6]
# print('before')
# print(new_list)
# n = 3    #element to be removed
# m = new_list.count(n)
# for i in range(m) :
#     new_list.remove(n)
# print('after')
# print(new_list)

###################################################

# 8. Program to remove all elements in a range from the List.

# str = input("Enter a string: ")
# num = input('Enter a range: ')
# nums1 = num.split()
# nums2 = [int(i) for i in nums1]
# res = ''
# for i in range(len(str)) :
#     if i>=nums2[0] and i<=nums2[1] :
#         pass
#     else :
#         res+=str[i]
# print(res)

###################################################

# 9. Program to Print the index of first matched element of a list.

# new_list = [3, 9, 2, 3, 4, 6]
# n = 6
# for i in new_list :
#     if (i == n) :
#         print(new_list.index(i))
#         break

###################################################

# 10. Convert a string to integers list.

# str = input('Enter numbers ,use a space beween then: ')
# str1 = str.split()
# nums = [int(i) for i in str1]
# print(nums)

###################################################

# 11. Input comma separated elements, convert into list and print.

# str = input('Enter numbers ,use a comma(,) beween then: ')
# str1 = str.split(',')
# print(str1)

###################################################

# 12. Program to find the position of minimum and maximum elements of a list.

# new_list = [3, 95, 2, 1, 4, 17]
# max_ele = max(new_list)
# min_ele = min(new_list)
# print('Position of max element: ', new_list.index(max_ele))
# print('Position of min element: ', new_list.index(min_ele))

###################################################

# 13. Program to input, append and print the list elements.

# l = []
# n = int(input('Enter number of inputs you want to give: '))
# for i in range(n) :
#     ele = input()
#     l.append(ele)
# print(l)

###################################################

# 14. Program to sort the elements of given list in Ascending and Descending Order.

# new_list = [3, 95, 2, 1, 4, 17]
# new_list.sort()
# print(new_list)
# new_list.sort(reverse=True)
# print(new_list)

###################################################

# 15. Program to find the differences of two lists.

# list_one = [3, 95, 2, 1, 4, 17]
# list_two = [3, 5, 2, 4, 7]
# res_list = []

# for i in list_one :
#     if(not(i in list_two)) :   # also check for dup ele. { not(i in res_list) }
#         res_list.append(i)

# for i in list_two :
#     if(not(i in list_one)) :
#         res_list.append(i)

# print(res_list)

###################################################

# 16. Program to Create two lists with EVEN numbers and ODD numbers from a list.

# old_list = [3, 95, 2, 1, 4, 17]
# even_list = []
# odd_list = []

# for i in old_list :
#     if(i%2 == 0) :
#         even_list.append(i)
#     elif(i%2 != 0) :
#         odd_list.append(i)

# print(even_list)
# print(odd_list)

###################################################

# 17. Program to print all numbers which are divisible by M and N in the List.

# old_list = [3, 30, 21, 1, 45, 17]
# m = 3
# n = 5
# for i in old_list :
#     if( i%m==0 and i%n==0) :
#         print(i,' ',end='')

###################################################

# 18. Program to remove duplicate elements from the list.

# old_list = [3, 6, 9, 2, 3, 4, 6]
# nwl = []

# for i in old_list :
#     if(i in nwl) :
#         old_list.remove(i)
#     else :
#         nwl.append(i)
# print(old_list)

###################################################

# 19. Create a list from the specified start to end index of another list.

# old_list = [3, 6, 9, 2, 3, 4, 6]
# start_ind = 2
# end_ind = 4
# l= []
# for i in range(len(old_list)) :
#     if(start_ind>= i<=end_ind) :
#         l.append(old_list[i])
# print(l)

###################################################

# 20. print list after removing EVEN numbers.  

# old_list = [3, 6, 9, 2, 3, 4, 14, 29, 34]
# for i in old_list[:] :
#     if(i%2==0) :
#         ind = old_list.index(i)
#         old_list.__delitem__(ind)
# print(old_list)

###################################################

# 21. Iterate a list in reverse order.

# old_list = [3, 6, 9, 2, 3, 4, 14, 29, 34]
# old_list.sort(reverse=True)
# print(old_list)

###################################################

# 22. Create three lists of numbers, their squares and cubes.

# old_list = [1, 2, 3, 4, 5]
# nw_list1 = []
# nw_list2 = []

# for i in old_list : 
#     nw_list1.append(i**2)
#     nw_list2.append(i**3)
# print(nw_list1)
# print(nw_list2)


###################################################

# 23. Create two lists with first half and second half elements of a list.

# old_list = [1, 2, 3, 4, 5, 6]
# first_half = []
# second_half = []
# l = len(old_list)

# for i in range(l) :
#     if(l%2==0):
#         if(i<int(l/2)):
#             first_half.append(old_list[i])
#         else :
#             second_half.append(old_list[i])
#     else :
#         if(i<=int(l/2)):
#             first_half.append(old_list[i])
#         else :
#             second_half.append(old_list[i])
# print(first_half)
# print(second_half)

###################################################

# 24. print list after removing ODD numbers.

# old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

# for i in old_list[:] :
#     if(i%2 != 0 ) :
#         print(i)
#         old_list.remove(i)
# print(old_list)

# i=0
# while i<len(old_list) :
#     if(old_list[i]%2 != 0) :
#         old_list.remove(old_list[i])
#     else:
#         i+=1
# print(old_list)


# 99. WAP to delete a item from an list if exists but take the first occurance

# old_list = [2, 3, 5, 3, 9, 3, 3]
# item = 3 

# i=0
# flag = False
# while i<len(old_list) :
#     if old_list[i]==item :
#         if flag == True :
#             old_list.pop(i)
#         else :
#             flag=True
#     i+=1
# print(old_list)
