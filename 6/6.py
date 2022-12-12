def checkForDuplicates(string):
    seen_characters = set()
    for char in string:
        if char in seen_characters:
            return True
        seen_characters.add(char)
    return False


with open("6/input.txt") as f:
    input = f.read()
    for x in range(14, len(input)):
        buffer = input[x-14:x]
        if not checkForDuplicates(buffer):
            print(x, buffer)
            break