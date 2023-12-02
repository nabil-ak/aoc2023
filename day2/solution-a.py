ids = []

def check_set(set):
    for set in sets:
        for color in set.split(","):
            number = int(color.split()[0])
            if "blue" in color and number > 14:
                return False
            if "green" in color and number > 13:
                return False
            if "red" in color and number > 12:
                return False
    return True


with open("input.txt") as file:
    for game in file.readlines():
        id = game.split(":")[0].split()[1]
        sets = game.split(":")[1].split(";")

        if check_set(sets):
            ids.append(int(id))
        
                       

print(ids)
print(sum(ids))
