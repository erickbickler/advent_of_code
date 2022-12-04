INPUT_FILE = "input{}.txt".format("1")

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        lines = list(map(int, input_file.readlines()))
        increases = 0
        prev = sum(lines[0:3])
        for i in range(1, len(lines) - 1):
            print(prev)
            line = sum(lines[i: i + 3])
            if line > prev:
                increases += 1
            prev = line

    print(increases)
