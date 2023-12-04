
points = 0
with open("input.txt") as file:
    for card in file.readlines():
        numbers = card.split(":")[1].replace("\n","")
        
        winningNumbers = numbers.split("|")[0].split()
        haveNumbers = numbers.split("|")[1].split()

        counter = 0
        for number in haveNumbers:
            if number in winningNumbers:
                counter += 1
        
        if counter > 0:
            points+=2**(counter-1)
        
print(points)

