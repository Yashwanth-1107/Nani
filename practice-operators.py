#practice your own examples on operators with python 
# what are the operators in python ?
# there are total 7 operators 1) arithmetic 2)comparision 3)assignment 4)logical 5)bitwise 6)membership 7)identity 
  #  1) arithmetic operators +,-,/,%,*,//(floor division),**(exponentiation)
#2)comparision >,>=,<,<=,==,!=
#3)assignment +=,-=,/+,*=,//=,**=,=,:=
#4)logical and,or,not
#5)bitwise &(and),^(xor),|(or),~(not),<<(right shift),>>(left shift)
#6)membership operators in , not in
#7)identity operators is,is not

#  1) arithmetic operators +,-,/,%,*,//(floor division),**(exponentiation)
a=20
b=10

p=2
q=3

print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a*b)
print(p**q)
print(a//b)

#2)comparision >,>=,<,<=,==,!=

print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

#3)assignment +=,-=,/+,*=,//=,**=,=,:=
v = 10

v += 5   # a = a + 5
print(v)

v -= 3   # a = a - 3
print(v)

v *= 2   # a = a * 2
print(v)

v /= 4   # a = a / 4
print(v)

v //= 2  # floor division
print(v)

v **= 2  # power
print(v)

#4)logical and,or,not
x = True
y = False

print(x and y)  # True only if both are True
print(x or y)   # True if at least one is True
print(not x)    # reverse value

#5)bitwise &(and),^(xor),|(or),~(not),<<(right shift),>>(left shift)
j = 10   # 101
k = 3 
r = -6  # 011

print(j & k)   # AND -> 001 = 1
print(j | k)   # OR  -> 111 = 7
print(j ^ k)   # XOR -> 110 = 6
print(~r)      # NOT -> -(a+1)
print(j << 1)  # left shift
print(j >> 1)  # right shift

#6)membership operators in , not in

list1 = [1, 2, 3, 4]

print(2 in list1) # 'in' is check is exist or not
print(5 not in list1) # 'not in' is check is not exist or not


#7)identity operators is,is not
k = [1,2,3] # 'is' referal to same memory or not 
l = [1,2,3] # 'is not ' referal to not same memory or not
m = k

print(k is l)       # False (different memory)
print(k is m)       # True (same object)
print(k is not l)