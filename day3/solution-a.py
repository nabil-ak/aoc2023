matrix = []
partNumbers = []
# Parse input into an matrix
with open("input.txt") as file:
    for line in file.readlines():
        matrix.append(list("!"+line.replace("\n","")+"!"))

# Add ! as borders of the matrix
matrix.insert(0, list("!"*len(matrix[0])))
matrix.append(list("!"*len(matrix[0])))

stack = []
isPartNumber = False
for y in range(1, len(matrix)-1):
    for x in range(1, len(matrix[y])-1):
        if not str(matrix[y][x]).isdigit():
            if isPartNumber and stack:
                # number in stack is a partnumber
                partNumbers.append(int("".join(stack)))
                isPartNumber = False
            stack.clear()
            continue

        # Found a number
        neighbours = [matrix[y-1][x-1],
                    matrix[y-1][x],
                    matrix[y-1][x+1],
                    matrix[y][x-1],
                    matrix[y][x+1],
                    matrix[y+1][x-1],
                    matrix[y+1][x],
                    matrix[y+1][x+1]]

        if any(not neighbour.isalnum() and neighbour not in ["!", "."] for neighbour in neighbours):
            # Neighbour is a symbol
            isPartNumber = True
        
        stack.append(matrix[y][x])


print(partNumbers)
print(sum(partNumbers))



