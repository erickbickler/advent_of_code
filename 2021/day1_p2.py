import sys
sys.path.append('../')
import utils.request_handler as request_handler

INPUT_FILE = request_handler.create_input_file()

if __name__=="__main__":
    with open(INPUT_FILE, "r") as input_file:
        lines = list(map(int, input_file.readlines()))
        increases = 0
        prev = sum(lines[0:3])
        for i in range(1, len(lines) - 1):
            # print(prev)
            line = sum(lines[i: i + 3])
            if line > prev:
                increases += 1
            prev = line

    print(increases)
    request_handler.submit_answer(increases, 2)

