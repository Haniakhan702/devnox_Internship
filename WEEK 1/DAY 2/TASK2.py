#Check wether a number is prime or not
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



# Function to check anagrams
def anagram(str1, str2):

    if sorted(str1) == sorted(str2):
        return "Anagrams"
    else:
        return "Not Anagrams"

# Take input from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Display result
print(anagram(str1, str2))