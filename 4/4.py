
count = 0
with open("4/input.txt") as f:
    for line in f:
        pair = line.strip().split(",")
        first = pair[0].split("-")
        second = pair[1].split("-")
        # first is in second
        if int(first[1]) >= int(second[0]) and int(first[0]) <= int(second[1]):
            count += 1
        elif int(second[1]) >= int(first[0]) and int(second[0]) <= int(first[1]):
            count += 1

print(count)