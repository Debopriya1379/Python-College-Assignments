# 1. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
# salary, and house rent allowance is 20% of basic salary. Write a program to calculate
# his gross salary.
#########
# baseSal = int(input('Enter Basic salary : '))
# da = (baseSal*40)//100
# ra = (baseSal*20)//100
# gross = baseSal+da+ra
# print(f'Gross salary : {gross} rs')

#############################################################################

# 2. The distance between two cities (in km.) is input through the keyboard. Write a program to
# convert and print this distance in meters, feet, inches and centimeters.
# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks
# and percentage marks obtained by the student. Assume that the maximum marks that can be
# obtained by a student in each subject is 100.
# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program
# to convert this temperature into Centigrade degrees.
##########
# print("convert km to others---")
# dis_in_km = float(input("Enter distance in k.m. : "))
# dis_in_meter = dis_in_km*1000
# dis_in_centm = dis_in_meter*100
# dis_in_feet = dis_in_meter*3.28
# dis_in_inch = dis_in_meter*39.3701
# print("Distance in Meter: ",dis_in_meter,' meter')
# print("Distance in Centimeter: ",dis_in_centm,' centimeter')
# print("Distance in Feet: ",dis_in_feet,' feet')
# print("Distance in Inch: ",dis_in_inch,' inch')

#############################################################################


# 3. The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle, and the area &
# circumference of the circle.
########
# print("Calculate Area and Perimeter of a Reactangle")
# length = int(input("Enter length of reactangle: "))
# breath = int(input("Enter breath of reactangle: "))
# area = length*breath
# perimeter = (length+breath)*2
# print("Area of the Rectangle = ",area)
# print("Perimeter of the Rectangle = ",perimeter)
# print("Calculate Areaa and Circumference of a Circle")
# rad = int(input("Enter circle radius: "))
# area_of_circle = ((rad**2)*22)/7
# circumference = ((rad*2)*22)/7
# print("Area of the circle = ", area_of_circle)
# print("Area of the circumference = ", circumference)

#############################################################################

# 4. Two numbers are input through the keyboard into two locations C and D. Write a program to
# interchange the contents of C and D.
##########
# C=int(input('Enter C : '))
# D=int(input('Enter D : '))
# temp = C
# C=D
# D=temp
# print(f'C = {C}')
# print(f'D = {D}')

#############################################################################

# 5. If a five-digit number is input through the keyboard, write a program to calculate the sum of
# its digits.
##########
# num = input('Enter a number : ')
# sum = 0
# for i in num :
#     sum+=int(i)
# print(sum)

#############################################################################

# 6. If a five-digit number is input through the keyboard, write a program to reverse the number.
########
# num = int(input('Enter a number : '))
# sum = 0
# while num>0 :
#     ele=num%10
#     sum=(sum*10)+ele
#     num//=10
# print(sum)

#############################################################################

# 7. If a four-digit number is input through the keyboard, write a program to obtain the sum of
# the first and last digit of this number.
##########
# num = int(input('Enter a number : '))
# l = len(str(num))
# lastDigit= num%10
# while num>0 :
#     firstDigit= num%10
#     num//=10
# print('sum of first and last digit : ',firstDigit+lastDigit)

#############################################################################

# 8. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total
# percentage of literate men is 35 of the total population, write a program to find the total
# number of illiterate men and women if the population of the town is 80,000.
######

# totalPop = 80000
# men = totalPop * 0.52
# toalLit = totalPop * 0.48
# litMen = totalPop * 0.35
# totalIlit = totalPop-toalLit
# totalWomen = totalPop - men
# illMen = totalPop-litMen
# litWomen = toalLit-litMen
# illWomen = totalPop-litWomen
# print(illMen)
# print(illWomen)

#############################################################################

# 9. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be
# withdrawn is input through the keyboard in hundreds, find the total number of currency notes
# of each denomination the cashier will have to give to the withdrawer.
#######+
# ammount = int(input('Enter Ammount : '))
# countOne,countTwo,countThree=0,0,0
# if ammount>=100 :
#     countOne = ammount//100
#     ammount-=100*countOne
# if ammount>=50 :
#     countTwo = ammount//50
#     ammount-=50*countTwo
# if ammount>=10 :
#     countThree = ammount//10
#     ammount-=10*countThree
# print('100 : ',countOne)
# print('50 : ',countTwo)
# print('10 : ',countThree)

#############################################################################

# 10. If the total selling price of 15 items and the total profit earned on them is input through the
# keyboard, write a program to find the cost price of one item.

# totalPrice = int(input('Enter total price : '))
# totalProfit = int(input("Enter total Profit : "))
# totalCost = (totalPrice-totalProfit)//15
# print(totalCost)

#############################################################################

# 11. If a five-digit number is input through the keyboard, write a program to print a new number
# by adding one to each of its digits. For example if the number that is input is 12391 then the
# output should be displayed as 23402.

# num = input('Enter a number : ')
# nwNum=''
# for i in num :
#     j=int(i)
#     if j==9 :
#         nwNum+='0'
#     else :
#         nwNum+=str(j+1)
# print(nwNum)

