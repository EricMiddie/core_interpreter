class Fac:
    def __init__(self, tokenizer):
        # Choices: op, multiplication
        self.tokenizer = tokenizer
        self.op = None
        self.fac = None

    def ParseFac(self):
        self.op = Op(self.tokenizer)
        # <int> | <id> | (<exp>) are possibilities
        self.op.ParseOp()

class Op:
    def __init__(self, tokenizer):
        # Choices: int, id, expression
        self.tokenizer = tokenizer
        self.type = None
        self.value = None
    def ParseOp(self):
        currToken = self.tokenizer.getToken()


class CompOp:
    def __init__(self, operator):
        # Choices: !=, ==, <, >, <=, >=
        self.operator = operator