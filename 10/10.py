# input = open("10/input.txt", "r")

# data = input.read()

# data_list = data.split("\n")

# x = 1
# cycles = 0 
# total = 0 
# processing = False
# line = 0 
# for i in range(240):
#     if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
#         total += (cycles*x)
#     if processing == False:
#         if data_list[line] == "noop":
#             cycles += 1
#             line += 1
#         elif data_list[line][:4] == "addx":
#             processing = True
#             cycles += 1
#     elif processing == True:
#         cycles += 1
#         x += int(data_list[line][4:])
#         line += 1
#         processing = False
    

# print()   
# print(cycles)
# print(total)
print(sum((i+1)*(sum(a[:i])+1) for i,a in enumerate(zip(*([int(s.strip("nopadx") or 0)]*240 for s in open('10/input.txt').read().split()))) if i%40==19))
print("\n".join(l[40*i:40*i+40] for i,l in zip(range(6),["".join(".#"[0<=i%40-sum(a[:i])<3] for i,a in enumerate(zip(*([int(s.strip("nopadx") or 0)]*240 for s in open('10/input.txt').read().split()))))]*6)))