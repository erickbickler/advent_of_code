INPUT_FILE = "input{}.txt".format("11")

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file.read().splitlines():