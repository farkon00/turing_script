from __future__ import annotations

from enum import Enum, auto

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