class CompOp:
    def __init__(self, tokenizer):
        # Choices: !=, ==, <, >, <=, >=
        self.tokenizer = tokenizer
        self.operator = None
        self.string_operator = None

    def ParseCompOp(self):
        # Check that the token is one of the valid choices specified in the BNF
        if self.tokenizer.getToken() not in [25, 26, 27, 28, 29, 30]:
            print("Parse Error: Exxpected comparator")
            exit()
        # Save both the token and string representation of the token
        self.operator = self.tokenizer.getToken()
        self.string_operator = self.tokenizer.tokenName()
        # Skip the Token
        self.tokenizer.skipToken()

    def PrintCompOp(self, currentTab):
        # print the comp op in line
        tabs = '\t' * currentTab
        print(f"{tabs} {self.string_operator} ", end='')

    def EvalCompOp(self):
        # returns the token value (int)
        return self.operator