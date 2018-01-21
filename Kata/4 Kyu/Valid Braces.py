def validBraces(string):
    while len(string) > 0 and "()" in string or "[]" in string or "{}" in string:
        string = string.replace("()","").replace("[]","").replace("{}","")
    return len(string) == 0