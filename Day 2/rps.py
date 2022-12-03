# {opp move [A,B,C]} {your move [X,Y,Z]}
# ###PART 1###
# A = ROCK = 1 
# B = PAPER = 2
# C = SCISSORS = 3

# X = ROCK = 1
# Y = PAPER = 2
# Z = SCISSORS = 3

# score = {move score} + {win score [0 loss, 3 draw, 6 win]}
# part 2
# X = need lose
# Y = need draw
# Z = need win
win_loss_compbinations1 = {"AX": 4, "AY": 8, "AZ": 3,
                          "BX": 1, "BY": 5, "BZ":9,
                          "CX": 7, "CY": 2, "CZ": 6}
win_loss_combinations2 = {"AX": 3, "AY": 4, "AZ": 8,




                          "BX": 1, "BY": 5, "BZ":9,
                          "CX": 2, "CY": 6, "CZ": 7}


def part1():
    score1 = 0
    with open("input.txt") as f:
        for line in f: score1 += win_loss_compbinations1[line.replace(" ", "").strip()]

    print(f"Total Score: {score1}")
def part2():

    score2 = 0 
    with open("input.txt") as f: 
        for line in f: score2 += win_loss_combinations2[line.replace(" ", "").strip()]    

    print(f"Score: {score2}")


part1()
part2()         