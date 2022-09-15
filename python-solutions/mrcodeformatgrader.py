from operator import itemgetter
from itertools import groupby


def print_range_list(range_list):
    output = ""
    l = len(range_list)
    for i, t in enumerate(range_list):
        if i > 0 and i+2 == l:
            if t[0] == t[1]:
                output += "{} and ".format(t[0])
            else:
                output += "{}-{} and ".format(t[0],t[1])
        elif i+1 == l:
            if t[0] == t[1]:
                output += "{}".format(t[0])
            else:
                output += "{}-{}".format(t[0],t[1])
        else:
            if t[0] == t[1]:
                output += "{}, ".format(t[0])
            else:
                output += "{}-{}, ".format(t[0],t[1])
    return output
        

def main():
    lines, error_lines = map(int, input().split())
    errors_list = list(map(int,input().split()))
    errors_set = set(errors_list)
    correct_list = []
    for i in range(1, lines+1):
        if i not in errors_set:
            correct_list.append(i)
    error_ranges = []
    correct_ranges = [] 
    for _, g in groupby(enumerate(errors_list), lambda x:x[0]-x[1]):
        r = list(map(itemgetter(1),g))
        error_ranges.append((r[0],r[-1]))

    for _, g in groupby(enumerate(correct_list), lambda x:x[0]-x[1]):
        r = list(map(itemgetter(1), g))
        correct_ranges.append((r[0],r[-1]))
    
    print("Errors:", print_range_list(error_ranges))
    print("Correct:", print_range_list(correct_ranges))





if __name__ == "__main__":
    main()
