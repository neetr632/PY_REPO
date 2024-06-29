# returns a numbers between 5 and 10 (both are included) 
import random
print(random.randint(5,10))

#returns a number between 3 (included) and 9 (not included)
print(random.randrange(3,9))

#python random choice() method
l = ["apple","banana","cherry"]
print(random.choice(l))

r = random.random()
print(r) # returns a float value between 0 and 1

lc = [1,2,14,3,245,3,64,45,36,3,453,62,556,25]
random.shuffle(lc)
print(lc)

uniform = random.uniform(3,9)
print(uniform)