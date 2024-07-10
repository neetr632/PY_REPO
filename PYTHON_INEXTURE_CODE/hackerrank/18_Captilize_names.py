import re

def solve(s):
    # Define a regex pattern to match words separated by spaces
    pattern = r'(?<!\d)\b\w+\b'
    
    # Function to capitalize matched words
    def capitalize_word(match):
        return match.group(0).capitalize()
    
    # Use re.sub() with a function to apply the capitalization
    result = re.sub(pattern, capitalize_word, s)
    
    return result

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
