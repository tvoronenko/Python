# This Python file uses the following encoding: utf-8
def remove_dupl(str):
    result =[]
    checker = 0
    for c in str:
        val = ord(c)
        offset = 1 << val
        if (checker & offset )==0:
            result.append(c)
            checker|=offset
    return ''.join(result)

print(remove_dupl('dffetg!3365~~'))