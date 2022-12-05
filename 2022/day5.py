INPUT_FILE = "input{}.txt".format("5")

s1 = ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M']
s2 = ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H']
s3 = ['W', 'R', 'C', 'D', 'G']
s4 = ['N', 'B', 'S']
s5 = ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N']
s6 = ['P', 'R', 'M', 'W']
s7 = ['R', 'T', 'N', 'G', 'L', 'S', 'W']
s8 = ['Q', 'T', 'H', 'F', 'N', 'B', 'V']
s9 = ['L', 'M', 'H', 'Z', 'N', 'F']

stacks = [s1, s2, s3, s4, s5, s6, s7,s8,s9]

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        lines = input_file.read().splitlines()
        for line in lines[10:]:
            move = line.split()
            num = int(move[1])
            origin = int(move[3])-1
            dest = int(move[5]) -1

            for i in stacks[origin][-1 * num:]:
                stacks[dest].append(i)
            stacks[origin] = stacks[origin][:-1 * num]

    print([i[-1] for i in stacks])