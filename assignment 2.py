# task 1 - check if the number is odd or even

a =int(input("enter the first number"))
if (a % 2 == 0):
    print(a, "is an even number")
else:
    print(a,"is an odd number")

# task 2 - sum of all integers in 1 to 50
n=50
sum = 0
i = 1

while(i <= n):
    sum += i
    i +=1
    print(sum)




