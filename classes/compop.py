class CompOp:
    def __init__(self, tokenizer):
        # Choices: !=, ==, <, >, <=, >=
        self.tokenizer = tokenizer
        self.operator = None

    def ParseCompOp(self):
        if self.tokenizer.getToken() not in [25, 26, 27, 28, 29, 30]:
            print("Parse Error: Exxpected comparator")
            exit()
        self.operator = self.tokenizer.getToken()
        self.tokenizer.skipToken()