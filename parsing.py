def find_blocks(code : str) -> tuple[list[int], list[int]]:
    """Finds blocks in code"""
    opening_backets = []
    closing_backets = []
    for i in range(len(code)):
        if code[i] == '{':
            opening_backets.append(i)
        elif code[i] == '}':
            closing_backets.append(i)

    return opening_backets, closing_backets

def parse_code(code : str):
    """Parses code into operations"""
    ops = []

    opening_brackets, closing_brackets = find_blocks(code)

    return ops