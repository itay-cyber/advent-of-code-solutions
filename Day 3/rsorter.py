from itertools import islice

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

def part1():
    sum = 0
    with open("input.txt") as f:
        for line in f:
            compartment1, compartment2 = line[0:len(line) // 2], line[len(line) // 2:]
            shared_item_type = ''
            for char in compartment1:
                if char in compartment2:
                    shared_item_type = char
            sum += priorities[shared_item_type]


    print(sum)
def part2():
    with open("input.txt") as f:
        data = f.read()
        splitlist = data.split("\n")
        groupcount = 0
        group = []
        sum = 0
        while splitlist != []:
            group = []
            for i in range(3):
                if splitlist != []:
                    group.append(splitlist.pop())
            
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    sum += priorities[char]
                    break
            groupcount += 1
    print(f"Gcount: {groupcount} Sum: {sum}")     
part2()
