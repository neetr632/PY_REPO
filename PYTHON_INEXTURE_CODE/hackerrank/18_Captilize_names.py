import re
pattern = r"^(?!\d).*"
def solve(s):
    results = []
    for x in s.split():
        filtered_text = re.findall(pattern, x)
        if filtered_text:
            result = " ".join(filtered_text)
            result = result.title()  
            results.append(result)
        return " ".join(results)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
