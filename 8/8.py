input = open("8/input.txt").readlines()

forest = [[int(t) for t in row.strip()] for row in input]
h, w = len(forest), len(forest[0])

vis_count = 0
for x in range(w):
    col = [forest[i][x] for i in range(h)]
    for y in range(h):
        row = forest[y]
        this = forest[y][x]
        vis_count += (
            all(t < this for t in row[:x])
            or all(t < this for t in row[x + 1 :])
            or all(t < this for t in col[:y])
            or all(t < this for t in col[y + 1 :])
        )

high_score = 0
for x in range(w):
    col = [forest[i][x] for i in range(h)]
    for y in range(h):
        row = forest[y]
        this = row[x]
        dist_l = next((d for d in range(1, x) if row[x - d] >= this), x)
        dist_r = next((d for d in range(1, w - x) if row[x + d] >= this), w - x - 1)
        dist_u = next((d for d in range(1, y) if col[y - d] >= this), y)
        dist_d = next((d for d in range(1, h - y) if col[y + d] >= this), h - y - 1)
        high_score = max(high_score, dist_l * dist_r * dist_u * dist_d)

print(f"Day 8 - Result 1: {vis_count}")
print(f"Day 8 - Result 2: {high_score}")


# map = []
# visibleCount = 0
# treeScores = []


# with open("8/test.txt") as f:
#     map = [line.strip() for line in f]

# def is_visible(x, y):
#     visible = False
#     currTree = int(map[x][y])
#     if x == 0 or y == 0 or x == len(map) - 1 or y == len(map) - 1: #edge
#         visible = True
#     else:
#         visibleLeft = visibleRight = visibleUp = visibleDown = True
#         for i in range(x): #check left
#             if (int(map[i][y])) >= currTree:
#                 visibleLeft = False
#         for i in range(x+1, len(map)): #check right
#             if (int(map[i][y])) >= currTree:
#                 visibleRight = False
#         for i in range(y): #check up
#             if (int(map[x][i])) >= currTree:
#                 visibleUp = False
#         for i in range(y+1, len(map)): #check down
#             if (int(map[x][i])) >= currTree:
#                 visibleDown = False
#         if(visibleLeft or visibleRight or visibleUp or visibleDown):
#             visible = True
#     return(visible)

# def get_tree_score(x, y):
#     totalScore = scoreLeft = scoreRight = scoreUp = scoreDown = 0
#     isBlockedLeft = isBlockedRight = isBlockedUp = isBlockedDown = False
#     l = x - 1
#     r = x + 1
#     u = y - 1
#     d = y + 1
#     currTree = int(map[x][y])
#     while l >= 0 and isBlockedLeft == False: #check left
#         if(currTree > int(map[l][y])):
#             scoreLeft += 1
#             l -= 1
#         else:
#             isBlockedLeft = True
#     while r < len(map) and isBlockedRight == False: #check right
#         if(currTree > int(map[r][y])):
#             scoreRight += 1
#             r += 1
#         else:
#             isBlockedRight = True
#     while u >= 0 and isBlockedUp == False: #check up
#         if(currTree > int(map[x][u])):
#             scoreUp += 1
#             u -= 1
#         else:
#             isBlockedUp = True        
#     while d < len(map) and isBlockedDown == False: #check down
#         if(currTree > int(map[x][d])):
#             scoreDown += 1
#             d += 1
#         else:
#             isBlockedDown = True
            
#     totalScore = scoreLeft * scoreRight * scoreUp * scoreDown
            
#     return(totalScore)

# for x in range(len(map)):
#     for y in range(len(map)):
#         if is_visible(x, y):
#             visibleCount += 1
#         treeScores.append(get_tree_score(x, y))
# print(visibleCount, max(treeScores))