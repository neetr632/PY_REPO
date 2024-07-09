import textwrap
def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped) # Returning the output as a single string with new lines characters embedded

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)