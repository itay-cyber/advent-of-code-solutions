cols = [
    ["W", "M", "L", "F"], #1 
    ["B", "Z", "V", "M", "F"], #2
    ["H", "V", "R", "S", "L", "Q"], #3
    ["F", "S", "V", "Q", "P", "M", "T", "J"], #4
    ["L", "S", "W"], #5
    ["F", "V", "P", "M", "R", "J", "W"], #6
    ["J", "Q", "C", "P", "N", "R", "F"], #7
    ["V", "H", "P", "S", "Z", "W", "R", "B"],#8
    ["B", "M", "J", "C", "G", "H", "Z", "W"]#9
]
def part1():
    with open("directions.txt") as f:
        for line in f:
            processed = line.strip().replace("move ", "").replace("from ", "-").replace("to ", "-").split("-")
            quantity = int(processed[0])
            startloc, endloc = int(processed[1]), int(processed[2])
            for i in range(quantity):
                cols[endloc - 1].append(cols[startloc-1].pop())
        
    for i in range(len(cols)):
        print(cols[i]) 

def part2():
    with open("directions.txt") as f:
        for line in f:
            processed = line.strip().replace("move ", "").replace("from ", "-").replace("to ", "-").split("-")
            quantity = int(processed[0])
            startloc, endloc = int(processed[1]), int(processed[2])

            toAppend = cols[startloc-1][-quantity:]
            print(f"TOapp: " + str(toAppend))

            for i in toAppend:
                cols[endloc - 1].append(i)  

            for i in range(quantity):
                cols[startloc-1].pop()         
    for i in range(len(cols)):
        print(cols[i])
        
part2()