import os

here = os.path.dirname(os.path.abspath(__file__))

# File contents are A C\n
# A=Rock, B=Paper, C=Scissors
# X=Rock, Y=Paper, Z=Scissors
# Score: A=1, B=2, C=3; lost=0, 3=tie, 6=win
# A ties X = 4
# A loses Y = 1
# A wins Z = 7
# B ties Y = 5
# B loses Z = 2
# B wins X = 8
# C ties Z = 6
# C loses X = 3
# C wins Y = 9
filename = os.path.join(here, "input.txt")
with open(filename, "r") as inputData:
    contents = inputData.readlines()

results = {
    "AX" : 4,
    "AY" : 1,
    "AZ" : 7,
    "BY" : 5,
    "BZ" : 2,
    "BX" : 8,
    "CZ" : 6,
    "CX" : 3,
    "CY" : 9
}
currentRound = []
rounds = []
for line in contents:
    rounds.append(''.join(line.split()))

print(rounds.count())

totalScore = 0
for round in rounds:
    #print(round)
    #print (results[round])
    totalScore += results[round]
    
print(totalScore)