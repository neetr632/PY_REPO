def mutate_string(string, position, character):
    string_list = []
    for i in string:
        string_list.append(i)
    string_list[position]=character
    modified_string = ''.join(map(str, string_list)) 
    return modified_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)