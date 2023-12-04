
cardMap = {}

with open("input.txt") as file:
    for i, card in enumerate(file.readlines()):
        if i+1 in cardMap:
            cardMap[i+1] += 1
        else:
            cardMap[i+1] = 1

        numbers = card.split(":")[1].replace("\n","")
        
        winningNumbers = numbers.split("|")[0].split()
        haveNumbers = numbers.split("|")[1].split()

        counter = 0
        for number in haveNumbers:
            if number in winningNumbers:
                counter += 1
                
        for x in range(cardMap[i+1]):
            start = i+2
            for win in range(counter):
                if start in cardMap:
                    cardMap[start] += 1
                else:
                    cardMap[start] = 1
                start+=1
        
        
print(cardMap)

print(sum(cardMap.values()))

