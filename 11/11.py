
class Monkey:

    items = []
    operation  = ""
    testCase = int
    ifTrue = int
    ifFalse = int
    count = 0

    def __init__(self, nums, op, ts, tru, fal):
        self.items = nums
        self.operation = op
        self.testCase = ts
        self.ifTrue = tru
        self.ifFalse = fal


def setup(path):
    with open(path, "r") as f: input = f.read().split("\n\n")
    data = []
    monkeys = []
    for m in range(len(input)):
        data.append(input[m].strip().split("\n"))
        data[m].pop(0)
        data[m][0] = list(map(int, data[m][0][data[m][0].find(':') + 2:].split(",")))
        data[m][1] = data[m][1][data[m][1].find('=') + 2:]
        data[m][2] = int(data[m][2][data[m][2].find('y') + 2:])
        data[m][3] = int(data[m][3][data[m][3].find('y') + 2:])
        data[m][4] = int(data[m][4][data[m][4].find('y') + 2:])
        monkeys.append(Monkey(data[m][0], data[m][1], data[m][2], data[m][3], data[m][4]))
    return monkeys

monkeys = setup("11/input.txt")
supermodulo = 1
for monkey in monkeys:
    supermodulo *= monkey.testCase
print(supermodulo)

for round in range(10000):
    for m in monkeys:
        for x in range(len(m.items)):
            item = m.items[0]
            m.operation = m.operation.replace("old", "item")
            m.items[0] = eval(m.operation) % supermodulo
            if m.items[0] % m.testCase == 0: monkeys[m.ifTrue].items.append(m.items[0])
            else: monkeys[m.ifFalse].items.append(m.items[0])
            m.items.pop(0)
            m.count += 1
counters = []
for m in monkeys: counters.append(m.count)
counters.sort(reverse=True)
print("Part 2: ", counters[0]*counters[1])