import sys
sys.path.append('../')
import utils.request_handler as request_handler

INPUT_FILE_PATH = "inputs/input{}.txt".format("6")

def print_and_submit(answer, level):
    print(answer)
    request_handler.submit_answer(answer=answer, level=level)

def check(chars):
    for i in range(len(chars)):
        if chars[i] in chars[i + 1:]:
            return False
    # if chars[0] in chars[1:] or chars[1] in chars[2:] or chars[2] in chars[3:]:
    #     return False
    return True

with open(INPUT_FILE_PATH, "r") as input_file:
    length = 14
    line = input_file.read()
    for i in range(length, len(line)):
        nums = [line[i - j] for j in range(length)]
        if check(nums):
            print(i + 1)
            break

    # print_and_submit("", 1)
