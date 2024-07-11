import re 
text = "q, ert, 2, 4, 45, w1, 3d"

pattern = r"apple(?! pie)" 
# the negative assertion is matching the word with the space between the word and pie therefore it will print the two apple words. 

matches = re.findall(pattern, text)
print(matches)