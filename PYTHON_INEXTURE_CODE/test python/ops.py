a = 10
b = 3
c = 2
d = 55
e = 55.0
x = True
y = False
print(a**b**c)

c = a << 2
# binary shift from the LSB
print(d)

c = a & b  # 1010 &
# 0011
# 0010 = 2
print(c)
# atleast one bits need to be 1 to get a +ve result
c = a | b
print(c)  # 1011 = 11

c = a ^ b
print(c)  # 1001 = 9
# results are 1 when one of the two bits are same

print(d is e)

print(d == e)

print(x and y)
print(x or y)
print(not y)

print(a % b)  # returns the remainder of the division
print(a / b)  # returns the quotient as a floating-point number
print(a // b)  # returns the remainder as integer, rounded to the nearest integer
"""
Parentheses () - Highest precedence
Exponentiation **
Unary Operators +x, -x, ~x
Multiplication *, Division /, Floor Division //, Modulo %
Addition +, Subtraction -
Bitwise Shifts <<, >>
Bitwise AND &
Bitwise XOR ^
Bitwise OR |
Comparison Operators ==, !=, >, <, >=, <=, is, is not, in, not in
Logical NOT not
Logical AND and
Logical OR or - Lowest precedence among the logical operators
"""

x = 17 / 2 * 3 + 2
print(x)


y = 2 + 17 * (2 / 3)
print(y) 

z = 19 % 4 + 15 / 2 * 3
print(z)
# 3 + 22.5 = 25.5

q = ( 15 + 6 ) - 10 * 4
print(q)
# 21 - 40 = -19
w = 17 / 2 % 2 * 3**3
w1 = (17 / 2) % 2 * 3**3
#0.5 * 27
print(w1)
print(w)
print(w == w1)
a = 10
b = 3
c = 2
d = 4
e = 55.0
t = a ** b % c / d + e * b ** a
#59049
print(t)
u = a * b ** 2 + c ** 3
# 10*9+8
print(u)