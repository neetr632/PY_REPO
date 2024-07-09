import re #usage of regex module
string = str(input()) 
substring = str(input())

def findDuplicates(string, substring):
    pattern = f'(?={substring})' #  look_ahead assertion being used for finding overlapping patterns
    count = len(re.findall(pattern, string))  #findall method is used here for the counting of occurence
    return count

duplcates_found = findDuplicates(string, substring)
print(duplcates_found)