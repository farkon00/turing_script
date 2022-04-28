from __future__ import annotations

import sys

from enum import Enum, auto


class State:
    """Execution state class"""
    _instance = None

    def __init__(self, code) -> None:
        self.states = {}
        self.tape = [0] 
        self.code = code
        self.opers = parse_code(self.code)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

class OpIds(Enum):
    on = auto()
    colon = auto()
    not_colon = auto()
    state = auto()
    left = auto()
    right = auto()
    halt = auto()

class Oper:
    """Operation class"""
    def __init__(self, id: auto, args: list[Oper | str] = [], ops: list[Oper] = []) -> None:
        self.id = id
        self.args = args
        self.ops = []

def parse_code(code):
    """Parses code into operations"""
    # TODO Make parsing
    return []

def main():
    """Main function, excutes file"""
    if len(sys.argv) < 2:
        print("You didn't specify filename argument.")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        code = f.read()
    
    code = code.replace('\n', '')

    state = State(code)

    
    
if __name__ == "__main__":
    main()