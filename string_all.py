########### 3.WAP to remove i^th character of a string.

# str = input('Enter a string ')
# k = int(input('Enter the position you want to remove '))
# nw_str = ''
# for i in range(len(str)) :
#     if(i == k) :
#         continue
#     else :
#         nw_str += str[i]
# print(nw_str)

# def removeIth(str, i) :
#     a = str[ :i]
#     b = str[i+1: ]    
#     return a+b

# def removeIth(str, i) :
#     nw_str = str.replace(str[i], '', 1)
#     return nw_str

# n = input("Enter a string: ")
# m = int(input("Enter the index you want to remove: "))
# res = removeIth(n,m)
# print(res)

############### 4.WAP to calculate the length of a string, avoid space.

# str = input("Enter a string")
# len = 0
# for i in str :
#     if i == ' ' :
#         continue
#     len+=1

# print(len)

############### 5.WAP to print even length words in a string.

# str = input("Enter a sentence")
# str1 = str.split()

# for i in str1 :
#     if(len(i)%2 == 0) :
#         print(i)

############### 6.Write a program uppercase Half String.

# str = input("Enter a string: ")
# l = len(str)

# if(l%2==0) :
#     a = str[ :int(l/2)]
#     b = str[int(l/2) : ]
# else :
#     a = str[ :int(l/2)+1]
#     b = str[int(l/2)+1 : ]

# res = a.upper()+b
# print(res)

############### 7.Write a program to capitalize the first and last character of each word in a string

# str = input("Enter a sentence: ")
# str1 = str.split()
# nw_str = ''

# for i in str1 :
#     a = i[0:1]
#     b = i[1:-1]
#     c = i[-1: ]
#     d = a.upper()
#     e = c.upper()
#     nw_str += d+b+e+' '

# print(nw_str)

################# 8.Python program to check if a string has at least one letter and one number

#### 1st approach

# str = input('Enter a string: ')
# flag1 = False
# flag2 = False
# for i in str :
#     if(65<= ord(i) <=90 or 97<=ord(i)<=122) :
#         flag1 = True
#     if(48<= ord(i) <=57):
#         flag2 = True

# if(flag1== True & flag2==True) :
#     print('letter and number exists')
# elif(flag1==True) :
#     print('only letter exists')
# elif(flag2==True) :
#     print('only number exists')
# else :
#     print('letter and number does not exists')    

#### 2nd approach

# str = input('Enter a string: ')
# if str.isalnum() :
#     print('Alphabets and numbers exists')
# elif str.isalpha() :
#     print('Alphabets exists')
# elif str.isnumeric() :
#     print('Numbers exists')
# else :
#     print('Alphabets and numbers does not exists')

#################### 9.Write a program to accept the strings which contain all vowels

###### approach 1
# str = input('Enter a string: ')
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# flag = False
# for i in str :
#     if(not(i in vowels)) :
#         flag = True
# if(flag) :
#     print("This string cannot be accepted")
# else :
#     print("String accepted")

###### approach 2
# str = input('Enter a string: ')
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# for i in str :
#     if(not(i in vowels)) :
#         print("This string cannot be accepted")
#         break
# else :
#     print("String accepted")

################### 10.Write a program to count the Number of matching characters in a pair of string

# str1 = input('Enter string 1: ')
# str2 = input('Enter string 2: ')
# st1 = set(str1)
# st2 = set(str2)
# count = 0
# for i in st1 :
#     if(i in st2) :    
#         count += 1
# print(count)

################## 11.Write a program to remove all duplicates from a given string in Python, keeping the
# first character only

## without order
# str = input('Enter a string: ')
# s = set(str)
# res = "".join(s)
# print(res)

## with order
# str = input('Enter a string: ')  
# t=""
# for i in str:
#     if(i in t):
#         pass  #continue forces the loop to start at the next iteration whereas pass means "there is no code to execute here" and will continue through the remainder of the loop body.
#     else:
#         t=t+i
# print(t)

#################### 12.Write a program to least Frequent Character in String

# str1 = input('Enter a string: ')  
# nw_dict = {}
# for i in str1:
#     if(i in nw_dict):
#         nw_dict[i] += 1
#     else:
#         nw_dict[i] = 1
# res = min(nw_dict, key = nw_dict.get)
# print(res)

################## 13.Write a program to maximum frequency character in String

# str1 = input('Enter a string: ')  
# nw_dict = {}
# for i in str1:
#     if(i in nw_dict):
#         nw_dict[i] += 1
#     else:
#         nw_dict[i] = 1
# res = max(nw_dict, key = nw_dict.get)
# print(res)

################## 14.Write a program to odd Frequency Characters

# str1 = input('Enter a string: ')  
# s = set(str1)
# l = []
# for i in s :
#     if(str1.count(i)%2!=0) :
#         l.append(i)
# print(l)

################# 15.Write a program to specific Characters Frequency in String List

## finding freq. of single character
# str1 = input('Enter a string: ')  
# chr1 = input('Enter a character: ')  
# l = str1.count(chr1)
# print(l)

## finding freq. of multiple characters
# str1 = input('Enter a string: ')  
# chr1 = input('Enter characters: ')  
# chr2 = chr1.split()
# l = []
# for i in chr2 :
#     l.append(str1.count(i))
# print(l)

################## 16.Write a program to frequency of numbers in String

# str1 = input('Enter a string: ')  
# s = set(str1)
# nw_dict = {}
# for i in s :
#     if( 48<=ord(i)<=57 ) :
#         nw_dict[i] = str1.count(i)
# print(nw_dict)

################# 17.Write a program to check if a string contains any special character

#### 1st approach
# str1 = input('Enter a string: ')  
# s='[@_!#$%^&*()<>?/\|}{~:]'    # 21 special chracters
# t = set(s)
# for i in str1 :
#     if(i in t) :
#         print('Special chracter exists')  
#         break  
# else : 
#     print('Special chracter does not exists')

#### 2nd approach
# str = input('Enter a string: ')
# for i in str :
#     if not i.isalnum() :
#         print('special character exists')
#         break
# else :
#     print('Special character does not exists')

################ 18.Write a program to generating random strings until a given string is generated

# import string
# import random
# s1 = input("enter the string:")
# n = len(s1)
# s2 = None
# char = string.digits+string.ascii_uppercase+string.ascii_lowercase
# c = 1
# while s1!=s2:
#     s2= ''.join(random.choice(char) for i in range(n))
#     c+=1
#     print(s2)
# print("target is matched after",c," attermpts")


# import random
# import string
# possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

# a=input('Enter a string: ')
# c=1
# while a != random:
#     b = ''.join(random.choice(possibleCharacters)for i in range(len(a)))
#     c=c+1
#     print(b)
#     if b==a:
#         print(a)
#         print("target is matched after",c," attermpts")
#         break

################# 19. Write a program to find words that are greater than the given length k

# str = input('Enter a sentence : ')
# str1 = str.split()

# given_length = 3

# for i in str1 :
#     if(len(i)>given_length) :
#         print(i)

################## 20.Write a program for removing i-th character from a string

# str = input('Enter a string : ')
# removing_index = int(input('Enter the index to be removed : '))
# new_str = ''
# for i in range(len(str)) :
#     if(i!=removing_index) :
#         new_str+=str[i]
# print(new_str)

################## 21.Write a program to split and join a string

# str = input('Enter a string : ')
# res2_str = ''
# for i in str :
#     res2_str= res2_str+i+'  '
# print(res2_str)

# res1_str = ''
# for i in res2_str :
#     if i != ' ' :
#         res1_str+=i
# print(res1_str)

#################### 22.Write a program to find all close matches of input string from a list   **********

# difflib.get_close_matches(word, possibilities, n, cutoff) accepts four parameters in which n, cutoff are optional. 
# word is a sequence for which close matches are desired, possibilities is a list of sequences against which to match word. 
# Optional argument n (default 3) is the maximum number of close matches to return, n must be greater than 0. 
# Optional argument cutoff (default 0.6) is a float in the range [0, 1]. Possibilities that don’t score at least that similar to word are ignored.
# The best (no more than n) matches among the possibilities are returned in a list, sorted by similarity score, most similar first.

# import difflib
# possibilities = ['python', 'java', 'javascript', 'string1', 'string2']
# print(possibilities)
# str = input('Enter a string : ')
# res = difflib.get_close_matches(str,possibilities)
# print(res)

#################### 23.Write a program to find uncommon words from two Strings

# str1 = input('Enter sentence 1 : ')
# str2 = input('Enter sentence 2 : ')
# l1 = str1.split()
# l2 = str2.split()
# res_list = []
# for i in l1 :
#     if(i not in l2) :
#         res_list.append(i)
# for i in l2 :
#     if(i not in l1) :
#         res_list.append(i)
# print(res_list)

#################### 24.Write a program to swap commas and dots in a String

# str1 = input('Enter a sentence : ')
# res_list = ''
# for i in str1 :
#     if( i==',') :
#         res_list+='.'
#     elif( i=='.') :
#         res_list+=','
#     else :
#         res_list+=i
# print(res_list)

#################### 25.Write a program to print permutation of a given string using inbuilt function

# import itertools
# str1 = input('Enter a string : ')
# l =list(itertools.permutations(str1))
# for i in l :
#     print(''.join(i))

##################### 26. Write a program to convert numeric words to numbers

# str = input('Enter number :')
# num = 0
# l = len(str)
# for i in str :
#     num = num * 10 + (ord(i) - 48 )
# print('The num',num)

##################### 27. Write a program find to word location in String   

# str = input('Enter a sentence :')
# wrd = input('Enter the word :')
# print(wrd,' starts at index ',str.find(wrd))

##################### 28. Write a program to find consecutive characters frequency

# str = input('Enter a string: ')
# nw_dict = {}

# for i in str :
#     if i == ' ' :
#         continue
#     if i in nw_dict :
#         nw_dict[i]+=1
#     else :
#         nw_dict[i]=1
# for i in nw_dict :
#     print (i,' occurs ',nw_dict[i],' times')

##################### 29. Write a program to preform string slicing in Python to rotate a string

# str = input('Enter a string: ')
# d = int(input('Enter no. of character you want to rotate: '))
# res_str1 = str[:d]
# res_str2 = str[d:]
# res_str3 = str[:len(str)-d]
# res_str4 = str[len(str)-d:]
# print('left rotation : ',res_str2+res_str1)
# print('left rotation : ',res_str4+res_str3)

##################### 30. Write a program to string slicing in Python to check if a string can become empty by recursive deletion

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.

# str = input('Enter whole string: ')
# sub = input('Enter sub string: ')
# nw_str = ''

# if(len(str)%len(sub) != 0) :
#     print('Reucursive deletion not possible')
# else :
#     l = len(str)//len(sub)
#     for i in range(l) :
#         nw_str += sub
#     else:
#         if(str==nw_str) :
#             print('Reucursive deletion possible')
#         else:
#             print('Reucursive deletion not possible')

##################### 31. Write a program to find minimum number of rotations to obtain actual string

# str1 = input('Enter the string: ')
# str2 = input('Enter the actual string: ')
# m = str1
# count1 = 0
# count2 = 0

# while True :
#     m = m[len(m)-1] + m[:len(m)-1]
#     if (m == str2) :
#         count1 +=1
#         break
#     else :
#         count1+=1
#         if count1>len(str2) :
#             break

# while True :
#     str1 = str1[1:len(str1)]+str1[0]
#     if (str1 == str2) :
#         count2 +=1
#         break
#     else :
#         count2+=1
#         if count2>len(str2) :
#             break

# if count1<len(str2) :
#     print(min(count1,count2))
# else :
#     print('Given strings are not of same kind')

##################### 32. Write a program to sort String list by K character frequency

# str_list = []
# n = int(input('Enter no of elements: '))
# for i in range(n) :
#     ele = input('Enter string: ')
#     str_list.append(ele)
# s = input('Enter the character: ')
# nw_dict = {}
# for i in str_list :
#     nw_dict[i] = i.count(s)
# res_list = sorted(nw_dict)
# print(res_list)


############ convert to uppercase
# str = 'a'
# print(ord(str))
# print(ord(str)-32)
# print(chr(ord(str)-32))
#################################


# 99. inp: balloon op : l ;2 ,o :2

# str = 'balloon'
# nw_dict = {}

# for i in str :
#     if i in nw_dict :
#         nw_dict[i]+=1
#     else :
#         nw_dict[i]=1
# print(nw_dict)
# for i in nw_dict :
#     if nw_dict[i] != 1 :
#         print (i,'=',nw_dict[i])
