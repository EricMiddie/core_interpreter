class Stmt:
    def __init__(self, type, content):
        self.type = type  # can be "assign", "if", "loop", "in", "out"
        self.content = content

class StmtSeq:
    def __init__(self):
        self.stmts = []

    def add_stmt(self, stmt):
        self.stmts.append(stmt)