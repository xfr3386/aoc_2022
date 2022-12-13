import os

here = os.path.dirname(os.path.abspath(__file__))

# File contents are A C\n
# A=Rock, B=Paper, C=Scissors
# X=Rock, Y=Paper, Z=Scissors
# Score: X=1, Y=2, Z=3; lost=0, 3=tie, 6=win
# A ties X = 4
# A loses Y = 8
# A wins Z = 3
# B ties Y = 5
# B loses Z = 9
# B wins X = 1
# C ties Z = 6
# C loses X = 7
# C wins Y = 2
filename = os.path.join(here, "input.txt")
with open(filename, "r") as inputData:
    contents = inputData.readlines()

results = {
    "AX" : 4,
    "AY" : 8,
    "AZ" : 3,
    "BY" : 5,
    "BZ" : 9,
    "BX" : 1,
    "CZ" : 6,
    "CX" : 7,
    "CY" : 2
}
currentRound = []
rounds = []
for line in contents:
    rounds.append(''.join(line.split()))

totalScore = 0
for round in rounds:
    #print(round)
    #print (results[round])
    totalScore += results[round]
    
print(totalScore)