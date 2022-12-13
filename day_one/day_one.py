import os

# Find the elf carrying the most calories
def part_one(contents):
    maxTotal = 0
    currentTotal = 0
    for line in contents:
        if line == "\n":
            if currentTotal > maxTotal:
                maxTotal = currentTotal
            currentTotal = 0
        else:
            currentTotal += int(line.split()[0])

    print(maxTotal)
    return

# Find the top 3 elves carrying the most calories
def part_two(contents):
    currentElfCalories = 0
    calorieCounts = []
    for line in contents:
        if line == "\n":
            calorieCounts.append(currentElfCalories)
            currentElfCalories = 0
        else:
            currentElfCalories += int(line.split()[0])

    calorieCounts.sort(reverse=1)
    most = calorieCounts[0]
    secondMost = calorieCounts[1]
    thirdMost = calorieCounts[2]
    print(most)
    print(secondMost)
    print(thirdMost)
    print(most+secondMost+thirdMost)
    return

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, "input.txt")
with open(filename, "r") as inputData:
    contents = inputData.readlines()

part_one(contents)
print("===========")
part_two(contents)