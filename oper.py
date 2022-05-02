from __future__ import annotations

from enum import Enum, auto

class OpId(Enum):
    on = auto()
    colon = auto()
    not_colon = auto()
    var = auto()
    inv = auto()
    left = auto()
    right = auto()
    halt = auto()

class Oper:
    """Operation class"""
    def __init__(self, id: auto, args: list[UnionType[Oper, str]] = [], ops: list[Oper] = []) -> None:
        self.id = id
        self.args = args
        self.ops = ops

    def __str__(self) -> str:
        return f"<Oper: id={self.id.name}" +\
            (" args=\n" + str([str(i) for i in self.args]) if self.args else "\n") +\
            (" ops=" + str([str(i) + "\n" for i in self.ops]) + ">" if self.ops else ">")