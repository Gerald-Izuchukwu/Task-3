# A python that sums up up two integers
# if the result is between 15 and 20, it returns 20
# if not it returns the answer
#

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enetr the second number: "))
sum = num1 + num2

if sum in range(15,20):
    print(int(20))
else:
    print(sum)