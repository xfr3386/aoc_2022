import os
#split string in two
#find duplicated characters
#add up values of chars, a-z = 1-26, A-Z = 27-52
#ord('a') - 96
#ord('A') - 38

def convert_char(char):
    if str.islower(char):
        return ord(char)-96
    else:
        return ord(char)-38

def part_one(contents):
    total = 0
    for line in contents:
        first_half  = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for x in first_half:
            if x in second_half:
                total += convert_char(x)
                break

    print(total)
    return

def part_two(contents_iter):
    total = 0
    shared = []
    for first in contents_iter:
        second = next(contents_iter)
        third = next(contents_iter)
        for x in first:
            if x != '\n' and x in second and shared.count(x) == 0:
                shared.append(x)
                continue
        for x in shared:
            if x in third:
                total += convert_char(x)
                break
        shared = []
    print(total)
    return

here = os.path.dirname(os.path.abspath(__file__))

# File contents are LHLRlCCvCLVgHPfCHtVjBGrBDNzWFBsBGBfscGsD
filename = os.path.join(here, "input.txt")
with open(filename, "r") as inputData:
    contents = inputData.readlines()

part_one(contents)
part_two(iter(contents))