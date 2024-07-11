import re

# Pattern to match strings that do not start with a digit
pattern = r"^(?!\d).*"

def solve(s):
    results = []
    for x in s.split():
        filtered_text = re.findall(pattern, x)
        # print(filtered_text)
        if filtered_text:
            result = " ".join(filtered_text)
            print(result)
            result = result.title()  # Capitalize the first letter of each word
            results.append(result)
    return " ".join(results)

# Example usage:    
s = input()
output = solve(s)
print(output)
