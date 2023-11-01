class Fac:
    def __init__(self, op, fac):
        # Choices: op, multiplication
        self.op = op
        self.fac = fac

class Op:
    def __init__(self, type, value):
        # Choices: int, id, expression
        self.type = type
        self.value = value

class CompOp:
    def __init__(self, operator):
        # Choices: !=, ==, <, >, <=, >=
        self.operator = operator