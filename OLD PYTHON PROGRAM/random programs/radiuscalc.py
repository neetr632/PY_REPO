import math
pi_value = math.pi          
r = int(input("Enter the value of radius: "))
area = pi_value * r**2
print("The total area of the circle is: " + str(area))

circumference = 2 * pi_value * r
print("The total circumference of the circle is: " + str(circumference))
