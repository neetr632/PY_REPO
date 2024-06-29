import math
square_less_than_500000 = [num for num in range(1,1001) if num*num < 500000]
print(square_less_than_500000)


sentence = "the quick brown fox jumps over the lazy dog"
vowels = "aeiou"

vowels_in_sentence = [char for char in sentence if char in vowels]
print(vowels_in_sentence)


squares_and_cubes = [i*i*i if i%2 else i*i for i in range(1, 21)]
print(squares_and_cubes)

dict_comprehension =  {num: math.sqrt(num) for num in range(1, 21)}
print(dict_comprehension)

list  = [x*x for x in range(21)]
print(list)