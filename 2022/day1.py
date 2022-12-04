INPUT_FILE = "input{}.txt".format("1")

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        totals = []
        total = 0
        for line in input_file.read().splitlines():
            if line:
                total += int(line)
            else:
                totals.append(total)
                total = 0
    totals.sort(reverse=True)
    print(sum(totals[:3]))
