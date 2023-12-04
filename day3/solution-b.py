matrix = []
# Parse input into an matrix
with open("input.txt") as file:
    for line in file.readlines():
        matrix.append(list("!"+line.replace("\n","")+"!"))

# Add ! as borders of the matrix
matrix.insert(0, list("!"*len(matrix[0])))
matrix.append(list("!"*len(matrix[0])))

stack = []
starmap = {}
starcords = []
for y in range(1, len(matrix)-1):
    for x in range(1, len(matrix[y])-1):
        if not str(matrix[y][x]).isdigit():
            #Current char is not a number
            if starcords and stack:
                for starcord in starcords:
                    if starcord in starmap:
                        starmap[starcord].append(int("".join(stack)))
                    else:
                        starmap[starcord] = [int("".join(stack))]
            stack.clear()
            starcords = []
            continue

        # Found a number
        neighbours = [[y-1,x-1],
                    [y-1,x],
                    [y-1,x+1],
                    [y,x-1],
                    [y,x+1],
                    [y+1,x-1],
                    [y+1,x],
                    [y+1,x+1]]
        

        for neighbour in neighbours:
            if matrix[neighbour[0]][neighbour[1]] == "*":
                # Neighbour is a *
                if f"{neighbour[0]},{neighbour[1]}" not in starcords:
                    starcords.append(f"{neighbour[0]},{neighbour[1]}")
            
        
        stack.append(matrix[y][x])


sumOfPartnumber = 0

for partNumber in starmap.values():
    if len(partNumber) == 2:
        sumOfPartnumber += (partNumber[0]*partNumber[1])

print(starmap)
print(sumOfPartnumber)



