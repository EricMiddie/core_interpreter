class CompOp:
    def __init__(self, tokenizer):
        # Choices: !=, ==, <, >, <=, >=
        self.tokenizer = tokenizer
        self.operator = None
        self.string_operator = None

    def ParseCompOp(self):
        if self.tokenizer.getToken() not in [25, 26, 27, 28, 29, 30]:
            print("Parse Error: Exxpected comparator")
            exit()
        self.operator = self.tokenizer.getToken()
        self.string_operator = self.tokenizer.tokenName()
        self.tokenizer.skipToken()

    def PrintCompOp(self, currentTab):
        tabs = '\t' * currentTab
        print(f"{tabs} {self.string_operator} ", end='')

    def EvalCompOp(self):
        return self.operator