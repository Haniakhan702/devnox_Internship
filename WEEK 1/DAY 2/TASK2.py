#intput from user
n = int(input("Enter a number: "))
#Numbers less than 2 are not prime numbers
if n < 2:
    print(" Not a Prime Number")
else:
    #check if the number is divisible by any number from 2 to n-1
    for i in range (2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number ")

        #Check if a string is palindrome or not
        text = input("Enter a string:")
        #check if string is same when reversed
        if text  == text [::-1]:
            #if both are same then it is polindrome
            print(text, "is a polindrome")
        else:
            print(text, "is not a polindrome")
