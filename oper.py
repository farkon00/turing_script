from __future__ import annotations

from enum import Enum, auto

class OpId(Enum):
    on = auto()
    colon = auto()
    not_colon = auto()
    set = auto()
    inv = auto()
    left = auto()
    right = auto()
    halt = auto()

class Oper:
    """Operation class"""
    def __init__(self, id: auto, args: list[Oper | str] = [], ops: list[Oper] = []) -> None:
        self.id = id
        self.args = args
        self.ops = []

    def __str__(self) -> str:
        return f"<Oper: id={self.id.name}" +\
            (" args=" + str(self.args) if self.args else "") +\
            (" ops=" + str([str(self.ops) for i in self.ops]) + ">" if self.ops else ">")