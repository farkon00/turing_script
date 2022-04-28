import sys

from oper import *

def parse_code(code : str):
    """Parses code into operations"""
    ops = []

    temp = code
    while temp != "":
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
            case "set":
                splited = line.split()

                if len(splited) < 2:
                    print("You didn't give enough arguments for set")
                    sys.exit(1)
                if "=" not in " ".join(splited[1:]):
                    print('"=" wasn`t found in set')
                    sys.exit(1)

                ops.append(Oper(OpId.set, args=" ".join(splited[1:]).split("=")))
            case "invert":
                splited = line.split()
                if len(splited) < 2:
                    print("You didn't give enough arguments for invert")
                    sys.exit(1)

                ops.append(Oper(OpId.inv, args=splited[1]))
            case "halt":
                ops.append(Oper(OpId.halt))
        
        temp = temp[line_end+1:]

    return ops