INPUT_FILE = "input{}.txt".format("4")

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        count = 0
        for line in input_file.read().splitlines():
            inp = line.split(',')
            s1 = list(map(int, inp[0].split('-')))
            s2 = list(map(int, inp[1].split('-')))
            print(inp, s1, s2)
            if s1[0] <= s2[0] and s1[1] >= s2[0]:
                count += 1
            elif s2[0] <= s1[0] and s2[1] >= s1[0]:
                count += 1

    print(count)