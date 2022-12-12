stacks = [['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'], 
['L', 'D', 'Z', 'Q', 'W', 'V'],
['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'], 
['R', 'D', 'H', 'F', 'J', 'V', 'B'], 
['Z', 'W', 'L', 'C'],
['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'], 
['J', 'R', 'L', 'V', 'M', 'B', 'S'], 
['D', 'P', 'J'], 
['D', 'C', 'N', 'W', 'V']]

# stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

with open("5/input.txt") as f:
    for line in f:
        seq = line.strip().split(" ")
        blocksMoving = int(seq[1])
        start = int(seq[3]) - 1
        to = int(seq[5]) - 1
        moving = stacks[start][len(stacks[start]) - (blocksMoving):]
        del stacks[start][len(stacks[start]) - (blocksMoving):]
        stacks[to].extend(moving)
        moving = []

for stack in stacks:
    print(stack[len(stack)-1])