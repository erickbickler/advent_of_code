INPUT_FILE = "input{}.txt".format("1")

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        lines = list(map(int, input_file.readlines()))
        increases = 0
        prev = lines[0]
        for i in range(1, len(lines)):
            if lines[i] > prev:
                print(prev, lines[i])
                increases += 1
            prev = lines[i]

    print(increases)
