import os

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
def part_one(contents):
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

    rounds = []
    for line in contents:
        rounds.append(''.join(line.split()))

    totalScore = 0
    for round in rounds:
        totalScore += results[round]
        
    print("part one: " + str(totalScore)) #10941
    return

def choose_winner(opponent):
    result = 0
    if opponent == 'A': # Rock
        result = 8 # Paper = 2+6
    elif opponent == 'B': # Paper
        result = 9 # Scissors = 3+6
    else: # Scissors
        result = 7 # Rock = 1+6
    return result

def choose_loser(opponent):
    result = 0
    if opponent == 'A': # Rock
        result = 3 # Scissors = 3+0
    elif opponent == 'B': # Paper
        result = 1 # Rock = 1+0
    else: # Scissors
        result = 2 # Paper = 2+0
    return result

def choose_tie(opponent):
    result = 0
    if opponent == 'A': # Rock
        result = 4 # Rock = 1+3
    elif opponent == 'B': # Paper
        result = 5 # Paper = 2+3
    else: # Scissors
        result = 6 # Scissors = 3+3
    return result

# A=Rock, B=Paper, C=Scissors
# X=Rock, Y=Paper, Z=Scissors
# X=lose, Y=draw, Z=win
# Score: X=1, Y=2, Z=3; lost=0, 3=tie, 6=win
# if it ends in X, you choose the lose option, and score based on that
# if it ends in Y, you choose the win option, and score based on that
# if it ends in Z, you choose the tie option, and score based on that
def part_two(contents):
    rounds = []
    for line in contents:
        rounds.append(''.join(line.split()))
    
    totalScore = 0
    for round in rounds:
        ending = round[1]
        opponent = round[0]
        if ending == 'X':
            totalScore += choose_loser(opponent)
        elif ending == 'Y':
            totalScore += choose_tie(opponent)
        else:
            totalScore += choose_winner(opponent)

    print("part two: " + str(totalScore))
    return
    
here = os.path.dirname(os.path.abspath(__file__))

# File contents are A C\n
# A=Rock, B=Paper, C=Scissors
filename = os.path.join(here, "input.txt")
with open(filename, "r") as inputData:
    contents = inputData.readlines()

part_one(contents)
part_two(contents)