class If:
    def __init__(self, cond, stmt_seq_then, stmt_seq_else=None):
        self.cond = cond
        self.stmt_seq_then = stmt_seq_then
        self.stmt_seq_else = stmt_seq_else