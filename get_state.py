import sys

def get_state(state, name):
    name = name.strip()
    if name in ("0", "1"):
        return int(name)
    
    if name not in state.states:
        print("You didn't define state : " + name)
        sys.exit(1)
    
    return state.states[name]