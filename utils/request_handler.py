import os
import requests
import json
from colorama import Fore, Style
from datetime import date

today = date(2021, 12, 1)

with open("../secrets.json", "r") as secrets_file:
    COOKIE = json.load(secrets_file)["cookie"]
HEADERS = {"cookie":f"session={COOKIE}"}
INPUT_FOLDER_NAME = "inputs"
INPUT_FILE_FORMAT = f"input{today.day}.txt"

INPUT_URL_PATH = f"https://adventofcode.com/{today.year}/day/{today.day}/input"
ANSWER_URL_PATH = f"https://adventofcode.com/{today.year}/day/{today.day}/answer"

def create_input_file():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", str(today.year), INPUT_FOLDER_NAME, INPUT_FILE_FORMAT)
    input = requests.get(INPUT_URL_PATH, headers=HEADERS)
    file = open(file_path, "w")
    file.write(input.text)
    file.close()
    return file_path
    
def submit_answer(answer, level):
    response = requests.post(ANSWER_URL_PATH, data={"level": level, "answer": answer}, headers=HEADERS)
    if "That's the right answer!" in response.text:
        print(f"{Fore.GREEN}SUCCESSFUL ANSWER!{Style.RESET_ALL}")
    elif "Did you already complete it?" in response.text:
        print(f"{Fore.YELLOW}ALREADY COMPLETED{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}ANSWER NOT CORRECT{Style.RESET_ALL}")