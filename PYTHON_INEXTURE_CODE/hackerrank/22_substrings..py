from collections import OrderedDict


def merge_the_tools(string, k):
    substring = []
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        od = OrderedDict()
        for j in substring:
            od[j] = None
        print(''.join(od.keys()) )


# if __name__ == '__main__':
string, k = input(), int(input())
merge_the_tools(string, k)
