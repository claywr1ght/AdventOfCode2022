import pandas as pd

data = pd.read_excel(r'input.xlsx')
themDF = pd.DataFrame(data, columns=['them'])
meDF = pd.DataFrame(data, columns=['me'])
score = 0
print ("range: 0 to ", len(themDF.index))
for j in range(0, len(themDF.index)):
    them = themDF.iloc[j][0]
    me = meDF.iloc[j][0]
    if me == 'X': #lose
        if them == 'A':
            score += 3
        elif them == 'B':
            score += 1
        elif them == 'C':
            score += 2
    elif me == 'Y': #draw
        score += 3
        if them == 'A':
            score += 1
        elif them == 'B':
            score += 2
        elif them == 'C':
            score += 3
    elif me == 'Z': #win
        score += 6
        if them == 'A':
            score += 2
        elif them == 'B':
            score += 3
        elif them == 'C':
            score += 1
        
print(score)

# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).