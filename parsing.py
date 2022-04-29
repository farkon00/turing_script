import sys

from oper import *

def parse_code(code: str):
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

                ops.append(Oper(OpId.inv, args=splited[1:]))
            case "on":
                parse_on(line, ops)
            case "halt":
                ops.append(Oper(OpId.halt))
        
        temp = temp[line_end+1:]

    return ops

def parse_on(line: str, ops: list[Oper]):
    cond_start = line.find("(")
    cond_end = line.find(")")
    if cond_start == -1 or cond_end == -1:
        print("You didn't close the condition")
    cond = line[cond_start+1:cond_end]
    cond = parse_cond(cond)

    ops_start = line.find("{")
    ops_end = line.rfind("}")
    inside_ops = line[ops_start+1:ops_end]
    inside_ops = parse_code(inside_ops)

    ops.append(Oper(OpId.on, args=[cond], ops=inside_ops))

def parse_cond(cond: str):
    """Parses condition from string to operation(colon or not_colon)"""

    if ":" not in cond:
        print("Colon wasn`t found in condition")

    colon_parts = cond.split(":", maxsplit=1)
    colon_parts[0] = colon_parts[0].strip()
    colon_parts[1] = colon_parts[1].strip()

    is_not_colon = colon_parts[0][-1] == "!"

    return Oper(OpId.not_colon if is_not_colon else OpId.colon, args=colon_parts)