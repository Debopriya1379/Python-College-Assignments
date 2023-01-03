# Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and
# continue)

prime_nums = [] 
for i in range(1,101):
    if i == 0 or i == 1 :
        continue
    else :
        for j in range(2,int(i/2)+1):
            if i%j == 0 :
                break
        else :
            prime_nums.append(i)


print(prime_nums)