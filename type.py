a=20
print(type(a))

b="yashwanth"
print(type(b))

y=3.5
print(type(y))

x="100"
print(type(x))

x=input("Enter any text/number :--")
print(type(x))


import ast

# 1. Get the input as text
user_input = input("Type anything: ")

try:
    # 2. Try to "extract" the real data from the text
    data = ast.literal_eval(user_input)
except:
    # 3. If it's just a word (like yash), keep it as text
    data = user_input

# 4. Show the result
print("The type is:", type(data))



  




