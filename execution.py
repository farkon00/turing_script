import sys

from oper import *
from get_state import get_state

def execute_opers(state, opers=None):
    for i in opers:
        state.is_halt = bool(execute_oper(state, i))
        
        state.tape[state.current_cell] = state.states["cell"]

        if state.is_halt: 
            return True
    state.states["_start"] = 0

def execute_main(state):
    state.states["_start"] = 1

    while not state.is_halt:
        execute_opers(state, state.opers)
    
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

        case OpId.set:
            state.states[op.args[0].strip()] = get_state(state, op.args[1])

        case OpId.inv:
            arg = op.args[0].strip()
            if arg not in state.states:
                print("You didn't define state : " + arg)
                sys.exit(1)
            state.states[arg] = int(not get_state(state, arg))

        case OpId.on:
            if execute_oper(state, op.args[0]):
                return execute_opers(state, op.ops)

        case OpId.colon:
            return int(get_state(state, op.args[0]) == get_state(state, op.args[1]))

        case OpId.not_colon:
            return int(get_state(state, op.args[0]) != get_state(state, op.args[1]))

        case OpId.halt:
            return True