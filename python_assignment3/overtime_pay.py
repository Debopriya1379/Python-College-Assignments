# without using array

print("Enter working hours of 5 workers")
total_overtime_pay = 0

for i in range(5):
    ele = int(input())
    if(ele > 40):
        overtime = ele-40
        total_overtime_pay += overtime*12
        # print("Overtime pay",total_overtime_pay)
        # total_overtime_pay = 0
        overtime = 0
    # else:
        # print("no overtime pay is required")

print("Total Overtime pay",total_overtime_pay)


# using array