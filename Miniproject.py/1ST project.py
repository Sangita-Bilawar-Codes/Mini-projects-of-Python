# 1.Write a programe to input user's first name and print it's length.
name = input("Enter your name:")
print("Name:",name)
print(len(name))


# 2. Write a programe to find the occurance of $ in a string'
str = "I do not have $ but Ali has $22.5"
print(str.count("$"))



# 3.Write a programe to check if a number entered by the user is odd or even.
number = int(input("Enter your number:")) 
if(number%2 == 0):
    print("Even")
else:
    print("Odd")



# 4. Write a programe to fin the greatest number of 3 numbers entered by user.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if(num1>num2 and num2>num3):
    print("First number is the greatest.")
elif(num2>num3):
    print("Second number is the greatest.")
else:
    print("Third number is the greatest.")


