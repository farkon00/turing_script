import sys

from oper import *

def parse_code(code : str):
    """Parses code into operations"""
    ops = []

    temp = code
    while temp != "":
        print(temp)
        temp = temp.strip()

        blocks = 0
        for j, i in enumerate(temp):
            if i == ";" and blocks == 0:
                line_end = j
                break
            elif i == "{":
                blocks += 1
            elif i == "}":
                blocks -= 1
        else:
            if blocks != 0:
                print("Not all blocks in your code was closed")
            else:
                print('Missing ";"')
            sys.exit(1)

        line = temp[:line_end]
        match line.split(maxsplit=1)[0]:
            case "left":
                ops.append(Oper(OpId.left))
            case "right":
                ops.append(Oper(OpId.right))
            case "halt":
                ops.append(Oper(OpId.halt))
        
        temp = temp[line_end+1:]

    return ops