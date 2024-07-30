from collections import OrderedDict


def merge_the_tools(string, k):
    od = OrderedDict()
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        for j in substring:
            od[j] = j
        print(od)


# if __name__ == '__main__':
string, k = input(), int(input())
merge_the_tools(string, k)
