import sys
sys.path.append('../')
import utils.request_handler as request_handler

INPUT_FILE_PATH = request_handler.create_input_file()

def print_and_submit(answer, level):
    print(answer)
    request_handler.submit_answer(answer=answer, level=level)

with open(INPUT_FILE_PATH, "r") as input_file:
    for line in input_file.read().splitlines():
        pass

    print_and_submit("", 1)
