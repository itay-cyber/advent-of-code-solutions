def part1():
    with open("input.txt") as f:
        ol = 0
        data = f.read()
        splitlist = data.split("\n")

        for i in range(len(splitlist)):
            element = splitlist[i]
            ranges = element.split(",")

            start_r1, end_r1 = int(ranges[0].split("-")[0]), int(
                ranges[0].split("-")[1])

            start_r2, end_r2 = int(ranges[1].split("-")[0]), int(
                ranges[1].split("-")[1])
            # part 2
            if start_r1 <= start_r2 and end_r1 >= end_r2 or start_r2 <= start_r1 and end_r2 >= end_r1:
                ol += 1
    print(ol)


def part2():
    with open("input.txt") as f:
        ol = 0
        data = f.read()
        splitlist = data.split("\n")

        for i in range(len(splitlist)):
            element = splitlist[i]
            ranges = element.split(",")

            start_r1, end_r1 = int(ranges[0].split("-")[0]), int(
                ranges[0].split("-")[1])

            start_r2, end_r2 = int(ranges[1].split("-")[0]), int(
                ranges[1].split("-")[1])

            # part 2
            if start_r1 <= end_r2 and end_r1 >= start_r2 or start_r2 <= end_r1 and end_r2 >= start_r1:
                ol += 1
    print(ol)


part1()
part2()
