INPUT_FILE = "example_input{}.txt".format("11")

def gen_adjacent_node(matrix_2d, node=(0,0)):
    rows = len(matrix_2d)
    columns = len(matrix_2d[0])
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            # check valid index
            if (0 <= node[0]+r < rows and 0 <= node[1]+c < columns):
                yield (node[0]+r, node[1]+c)

def combine_lists(list_2d):
    combined = []
    for l in list_2d:
        combined += l
    for i in combined:
        if i > 9:
            return True
    return False

def check_all_flash(list_2d):
    for i in list_2d:
        for j in i:
            if j != 0:
                return False
    return True

if __name__=="__main__":
    squids = []
    flashes = 0

    with open(INPUT_FILE, "r") as input_file:
        for line in input_file.readlines():
            squids.append(list(map(int, list(line.strip('\n')))))
    
    step = 0
    while(not check_all_flash(squids)):
        # increment by 1
        for row in range(len(squids)):
            for column in range(len(squids[row])):
                squids[row][column] += 1
        # flash
        while(combine_lists(squids)):
            # print('\n'.join(''.join(str(i) for i in l) for l in squids) + '\n')
            for row in range(len(squids)):
                for column in range(len(squids[row])):
                    if squids[row][column] > 9:
                        squids[row][column] = 0
                        flashes += 1
                        for x, y in gen_adjacent_node(squids, (row, column)):
                            if squids[x][y] != 0:
                                squids[x][y] += 1
        step += 1

    print("flashes", flashes)
    print("step", step)
                    