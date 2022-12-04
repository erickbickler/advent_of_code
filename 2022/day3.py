from itertools import zip_longest

INPUT_FILE = "input{}.txt".format("3")



if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        scores = []
        lines = input_file.read().splitlines()
        for index in range(0, len(lines), 3):
            sepLines = list(lines[index:index + 3])
            print(sepLines)
            samesies = []
            for i in sepLines[0]:
                for j in sepLines[1]:
                    for k in sepLines[2]:
                        if i == j == k:
                            samesies.append(i)
            print(samesies)
            scores.append(samesies[0])

        print(sum([ord(i) - 96 if i.lower() == i else ord(i) - 38 for i in scores]))