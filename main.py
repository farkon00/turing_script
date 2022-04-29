import sys

from pprint import pprint

from parsing import parse_code

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

    pprint([str(i) for i in state.opers])
    
if __name__ == "__main__":
    main()