import sys

from oper import *

def execute_opers(state):
    is_halt = False
    while not is_halt:
        for i in state.opers:
            is_halt = execute_oper(state, i)
            
            state.tape[state.current_cell] = state.states["cell"]

            if is_halt:
                break
    
    print("Final tape state:\n" + " ".join(str(i) for i in state.tape))

def execute_oper(state, op: Oper):
    match op.id:
        case OpId.left:
            state.current_cell -= 1
            if state.current_cell < 0:
                inp = input("Input left cell: ")
                try:
                    inp = int(bool(int(inp))) # Converts any number to 0 or 1
                except ValueError:
                    print("You didn't input number")
                    sys.exit(1)

                state.tape.insert(0, inp)
                state.current_cell = 0

            state.states["cell"] = state.tape[state.current_cell]

        case OpId.right:
            state.current_cell += 1
            if state.current_cell >= len(state.tape):
                inp = input("Input right cell: ")
                try:
                    inp = int(bool(int(inp))) # Converts any number to 0 or 1
                except ValueError:
                    print("You didn't input number")
                    sys.exit(1)

                state.tape.append(inp)

            state.states["cell"] = state.tape[state.current_cell]

        case OpId.inv:
            if op.args[0] not in state.states:
                print("You didn't define state : " + op.args[0])
                sys.exit(1)
            state.states[op.args[0]] = int(not state.states[op.args[0]])

        case OpId.halt:
            return True