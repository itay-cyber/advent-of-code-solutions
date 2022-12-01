# read input file line by line
# add line to list "temp numbers"
# if line is empty, new elf
# if not, continue reading


def sum_arr(array):
    sum = 0
    for i in array:
        sum += int(i)
    return sum

temp_numbers = []
sums = []
lineread = 0
with open("input.txt", "r") as f:
    for line in f:
        newline = line.strip()
        
        if newline == "":
            sums.append(sum_arr(temp_numbers))
            temp_numbers = []
        else:
            temp_numbers.append(int(newline))

sums.sort()
print(sums) 
# since this already prints the top three, there is no need for a coding solution, I just took the last three indices and added them together to get the answer.


