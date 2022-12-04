INPUT_FILE = './example_input10.txt'

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score = 0

def check(string):
    while(len(string) > 1):
        print(string)
        breakpoint()
        for index, c in enumerate(string):
            if c == matching[string[0]]:
                string = string[:index] + string[index + 1:]
                string = string[0:]
                break
    if len(string) == 0:
        return 0
    else:
        return scoring[string]
        

with open(INPUT_FILE, 'r') as input_file:
    for line in input_file.readlines():
        score += check(line)

print(score)
