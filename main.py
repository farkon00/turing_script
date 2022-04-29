import sys

from pprint import pprint

from parsing import parse_code
from execution import execute_opers

class State:
    """Execution state class"""
    _instance = None

    def __init__(self, code) -> None:
        self.states: dict[str, int] = {"cell" : 0}

        self.tape: list[int] = [0] 
        self.current_cell: int = 0

        self.code: str = code
        self.opers: list = parse_code(self.code)

        self.is_halt = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

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

    execute_opers(state, main=True)
    
if __name__ == "__main__":
    main()