#What does input() function return by default?
 #The input() function always returns a string (str) by default


#Write a program to take user name and print it.

x=input("Enter your name")
print(x)

#Take two numbers from user and print their sum.
x=input("Enter your first number:-- ")
y=input("Enter your second number:--")

#here we did type casting because input function by default is string ,to convert string to integer we taken int() 

x=int(x)
y=int(y)

print(x+y)

#What happens if you add two numbers taken by input() without casting?
x=input("Enter your first number:-- ")
y=input("Enter your second number:--")
print(x+y)

#output is side by side actually it is string concatenation



#Convert string "100" to integer.

x="100"
x=int(x)


# Convert integer 25 to string.
# Convert float 10.8 to int.
# Write a program to take age from user and convert it to int.
