#Q.1   Any year is entered through the keyboard, write a program to determine whether the year is
# leap or not. Use the logical operators ‘and’ or ‘or’.

# yr = int(input("Enter a year: "))

# if (yr%400==0) or (yr%100 != 0) and (yr%4==0):
#     print('Leap year')
# else :
#     print('Not a leap year')

##############################################################

# Q.2 An Insurance company follows following rules to calculate premium.
# a) If a person’s health is excellent and the person is between 25 and 35 years of age and lives in
# a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot
# exceed Rs. 2 lakhs.
# b) If a person satisfies all the above conditions except that the sex is female then the premium is
# Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
# c) If a person’s health is poor and the person is between 25 and 35 years of age and lives in a
# village and is a male hen the premium is Rs. 6 per thousand and his policy cannot exceed Rs.
# 10,000.
# d) In all other cases the person is not insured.
# Write a program to output whether the person should be insured or not, his/her premium rate
# and maximum amount for which he/she can be insured.

# health_status
# age
# livesInCity
# gender
# ammount
# interest

# if salisfies all but female then 3 per 1000 and ammount<100000
# if health==poor and age(25,35), village, male then 6 per 1000 and ammount<10000
# otherwise not insured

############
# print('Enter person details: ')
# health_status = int(input('Enter health status(excellent=0,good=1,poor=2): '))
# age = int(input('age : '))
# livesInCity = int(input('If lives in city put 1 otherwise 0 : '))
# gender = int(input('for male 1 and for female 0 : '))

# if (health_status=='excellent' and 25<=age<=35 and livesInCity==1 and gender==1) :
#     insured = True
#     max_ammout = 100000
#     interest = 4
# elif (health_status=='excellent' and 25<=age<=35 and livesInCity==1 and gender==0) :
#     insured = True
#     max_ammout = 100000
#     interest = 3
# elif (health_status=='poor' and 25<=age<=35 and livesInCity==0 and gender==1) :
#     insured = True
#     max_ammout = 10000
#     interest = 6
# else :
#     insured = False

# if insured==False :
#     print('Person not insured')
# else :
#     print('Person premium rate : ',interest)
#     print('Person max ammount : ',max_ammout)

###############################################################

# 3. A certain grade of steel is graded according to the following conditions:
# (i) Hardness must be greater than 50
# (ii) Carbon content must be less than 0.7
# (iii) Tensile strength must be greater than 5600
# The grades are as follows:
# Grade is 10 if all three conditions are met
# Grade is 9 if conditions (i) and (ii) are met
# Grade is 8 if conditions (ii) and (iii) are met
# Grade is 7 if conditions (i) and (iii) are met
# Grade is 6 if only one condition is met
# Grade is 5 if none of the conditions are met
# Write a program, which will require the user to give values of hardness, carbon content and tensile
# strength of the steel under consideration and output the grade of the steel.

##########
# hardness = int(input('Enter hardness(0 to 100): '))
# cc = float(input('Enter carbon content(0 t0 1): '))
# ts = int(input('Enter Tensile Strength: '))

# def checkHardness(h) :
#     if h>50 :
#         return True
#     else :
#         return False

# def checkCc(c) :
#     if c<0.7 :
#         return True
#     else :
#         return False

# def checkTs(s) :
#     if s>5600 :
#         return True
#     else :
#         return False

# if checkHardness(hardness) and checkCc(cc) and checkTs(ts) :
#     grade = 10
# elif checkHardness(hardness) and checkCc(cc) :
#     grade = 9
# elif checkCc(cc) and checkTs(ts) :
#     grade = 8
# elif checkHardness(hardness) and checkTs(ts) :
#     grade = 7
# elif checkHardness(hardness) or checkCc(cc) or checkTs(ts) :
#     grade = 6
# else :
#     grade = 5

# print(f'Grade : {grade}')

###############################################################

# 4. A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10
# days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days your
# membership will be cancelled. Write a program to accept the number of days the member is late to
# return the book and display the fine or the appropriate message.

##########

# dt = int(input('Enter number of late days : '))

# if dt<6 :
#     fine = .50
#     print(f'Your fine ammount is {fine} paisa')
# elif dt in range(6,11) :
#     fine = 1
#     print(f'Your fine ammount is {fine} rs')
# elif dt in range(11,31) :
#     fine = 5
#     print(f'Your fine ammount is {fine} rs')
# elif dt>30 :
#     print('Your membership has been cancelled')

###############################################################

# 5. If the three sides of a triangle are entered through the keyboard, write a program to check whether
# the triangle is valid or not. The triangle is valid if the sum of two sides is greater than the largest of
# the three sides.

#######

# nums = input('Enter edges : ').split()
# edges = [int(i) for i in nums]

# def checkValidity(edg) :
#     grt = max(edg)
#     sum=0
#     for i in edg :
#         if i!=grt :
#             sum+=i
#     if(sum>grt) :
#         return True
#     else :
#         return False

# if(checkValidity(edges)==True) : print('Valid')
# else : print('Invalid')

###############################################################

# 6. If the three sides of a triangle are entered through the keyboard, write a program to check whether
# the triangle is isosceles, equilateral, scalene or right angled triangle.

######

# print("Enter sides of the triangle")
# x = int(input("Enter first side : "))
# y = int(input("Enter second side : "))
# z = int(input("Enter third side : "))

# if( x==y==z ):
#     print("Equilateral")
# elif( x==y or y==z or z==x):
#     print("Isoscale")
# else:
#     print("Scalene")
# if (x**2+y**2==z**2) or (x**2+z**2==y**2) or (y**2+z**2==x**2) :
#     print('and Right Angled')

###############################################################

# 7. In a company, worker efficiency is determined on the basis of the time required for a worker to
# complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the worker is
# said to be highly efficient. If the time required by the worker is between 3 – 4 hours, then the worker 
# is ordered to improve speed. If the time taken is between 4 – 5 hours, the worker is given training to
# improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to
# leave the company. If the time taken by the worker is input through the keyboard, find the efficiency
# of the worker.

######

# tm = float(input('Enter hours count : '))

# if tm>=2.0 and  tm<3.0 :
#     print('Highly efficient')
# elif tm>=3.0 and tm<4.0 :
#     print('Improve speed')
# elif tm>=4 and tm<5.0 :
#     print('Training required')
# elif tm>=5.0 :
#     print('Leave company')

###############################################################

# 8. A university has the following rules for a student to qualify for a degree with A as the main
# subject and B as the subsidiary subject:
# (a) He should get 55 percent or more in A and 45 percent or more in B.
# (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he should get at
# least 45 percent in A.
# (c) If he gets less than 45 percent in B and 65 percent or more in A he is allowed to reappear in an
# examination in B to qualify.
# (d) In all other cases he is declared to have failed. Write a program to receive marks in A and B and
# Output whether the student has passed, failed or is allowed to reappear in B.

######

# A=float(input('Enter percentage of A: '))
# B=float(input('Enter percentage of B: '))

# if A>=55.0 and B>=45.0 :
#     print('Qualified')
# elif A>=45.0 and B>=55.0 : 
#     print('qualified')
# elif A>=65.0 and B<45.0 :
#     print('Allowed to reappear for B')
# else :
#     print('failed')

###############################################################

# 9. The policy followed by a company to process customer orders is given by the following rules:
# (a) If a customer order is less than or equal to that in stock and has credit is OK, supply has
# requirement.
# (b) If has credit is not OK do not supply. Send him intimation.
# (c) If has credit is Ok but the item in stock is less than has order, supply what is in stock. Intimate to
# him data the balance will be shipped.
# Write a Python program to implement the company policy.

######

# stock = 100
# order = int(input('Enter order : '))
# credit = False

# if credit == True :
#     if (order<=stock) :
#         print(f'{order} products has been shipped')
#     else :
#         print(f'{stock} products has been shipped')
# else :
#     print(f'sorry, cannot shipped order, credit is not ok')