INPUT_FILE = "input{}.txt".format("2")

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}

victoryMap = {
    "X": "C",
    "Y": "A",
    "Z": "B", 
}

reverseVictoryMap = {
    "A": 2,
    "B": 3,
    "C": 1
}

lossMap = {
    "A": 3,
    "B": 1,
    "C": 2
}

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        totalScore = 0
        for line in input_file.read().splitlines():
            line = line.split()

            if line[1] == "Y":
                totalScore += 3 + scores[line[0]]
            elif line[1] == "X":
                totalScore += lossMap[line[0]]
            elif line[1] == "Z":
                totalScore += reverseVictoryMap[line[0]] + 6


        print(totalScore)