numbermap = {
    "one":"1", 
    "two":"2", 
    "three":"3", 
    "four":"4", 
    "five":"5", 
    "six":"6", 
    "seven":"7", 
    "eight":"8", 
    "nine":"9"
}

def find_all_indexes(input_string, substring):
    return [i for i in range(len(input_string)) if input_string.startswith(substring, i)]

#very bad time complexity
with open("input.txt") as file:
    numbers = []
    for line in file.readlines():
        firstDigit = None
        lastDigit = None
        for i, element in enumerate(line):
            if element.isnumeric():
                firstDigit = element if firstDigit == None else firstDigit
                lastDigit = element
            for item in numbermap:
                if i in find_all_indexes(line, item):
                    firstDigit = numbermap[item] if firstDigit == None else firstDigit
                    lastDigit = numbermap[item]
        numbers.append(int(firstDigit+lastDigit))
    print(numbers)
    print(sum(numbers))
