#Input from user to find leap year
year = int(input("Enter a year: "))

#Check if it is a leap year
if (year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0):
    print(year, " is a leap year")
else:
    print(year ,"is not a leap year")



#Take input from user to find factorial
n = int(input("Enter a number: "))

#Initial fact is 1
fact = 1

#Check if n is negative
if n < 0:
    print("Factorial not found")

# fac of 0 is always 1
elif n == 0:
    print("factorial = 1")

 # calculate the fact
else:   
    for i in range(1, n+1):
        fact*=i
    print("Factorial =", fact)



#Take input to reverse a number 
num = int(input("Enter a number : "))

#Initialize the reversed number
reverse = 0
#To reversed thr number 
while num > 0:
    #Get the last digit 
    digit = num % 10

    # Add the last digit to the revesrsed number 
    reverse = reverse * 10 + digit

    # Remove the last digit from original number
    num = num // 10

print("Reversed Number= ",reverse)
