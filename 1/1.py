
inputtxt = open("input.txt","r")
total = 0
sum = []
for line in inputtxt:
    if line.strip():
        total += int(line)
    else:
        sum.append(total)
        total = 0
    
sum.sort(reverse=True)
print(sum[0] + sum[1] + sum[2])
inputtxt.close()