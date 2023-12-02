powers = []

def check_set(set):
    maxBlue = 0
    maxGreen = 0
    maxRed = 0
    for set in sets:
        for color in set.split(","):
            number = int(color.split()[0])
            if "blue" in color:
                maxBlue = number if maxBlue == 0 or maxBlue < number else maxBlue
            if "green" in color:
                maxGreen = number if maxGreen == 0 or maxGreen < number  else maxGreen
            if "red" in color:
                maxRed = number if maxRed == 0 or maxRed < number  else maxRed
    return maxBlue*maxGreen*maxRed


with open("input.txt") as file:
    for game in file.readlines():
        id = game.split(":")[0].split()[1]
        sets = game.split(":")[1].split(";")

        powers.append(check_set(sets))
        
                       

print(powers)
print(sum(powers))
