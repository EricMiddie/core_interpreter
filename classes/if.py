from classes.cond import Cond    

class If:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.cond = None
        self.stmt_seq_then = None
        self.stmt_seq_else = None
    
    def ParseIf(self):
        from classes.stmt import StmtSeq
        # check and skip the if, this is redundant
        if self.tokenizer.getToken() != 5:
            print("Parse Error: Expected IF to start with if")
            exit()
        self.tokenizer.skipToken()
        
        # Assign the condition and the statement sequence
        self.cond = Cond(self.tokenizer)
        self.stmt_seq_then = StmtSeq(self.tokenizer)

        # Parse the condition
        self.cond.ParseCond()

        # Check and skip the 'then'
        if self.tokenizer.getToken() != 6:
            print("Parse Error: Expected IF to start with if")
            exit()
        self.tokenizer.skipToken()

        # Parse the statement sequence
        self.stmt_seq_then.ParseStmtSeq()

        # Check if we are in the first branch
        # Next token is "end"
        if self.tokenizer.getToken() == 3:
            self.tokenizer.skipToken()
            # Check for and skip the ;
            if self.tokenizer.getToken() != 12:
                print("Parse Error: Expected ; after 'end'")
                exit()
            self.tokenizer.skipToken()
        else:   
            self.stmt_seq_else = StmtSeq(self.tokenizer)
            # We must be in the alt
            # Check for and skip the 'else'
            if self.tokenizer.getToken() != 7:
                print("Parse Error: Expected 'else'. Either you meant 'end;' or you're missing 'else'")
                exit()
            self.tokenizer.skipToken()
            self.stmt_seq_else.ParseStmtSeq()

            # Check for and skip the 'end'
            if self.tokenizer.getToken() != 3:
                print("Parse Error: Expected 'end' to end IF statement")
                exit()
            self.tokenizer.skipToken()

            # Check for and skip the ';'
            if self.tokenizer.getToken() != 12:
                print("Parse Error: Expected ';' after 'end'.")
                exit()
            self.tokenizer.skipToken()

    def PrintIf(self, currentTab):
        # Print the if that is tabbed over certain amount
        tabs = '\t' * currentTab
        print(f"{tabs}if ", end='')
        self.cond.PrintCond(0)
        # We want it to go to the next line here
        print(" then") 
        # Print the statement sequence with additional indent
        self.stmt_seq_then.PrintStmtSeq(currentTab + 1)
        # Print the else sequence if we are in the second branch
        if self.stmt_seq_else is not None:
            print(f"{tabs}else")
            self.stmt_seq_else.PrintStmtSeq(currentTab + 1)
        print(f"{tabs}end;")

    def ExecIf(self, datapoints):
        # Evaluate the condition and execute the corresponding statement sequence
        if self.cond.EvalCond(datapoints):
            self.stmt_seq_then.ExecStmtSeq(datapoints)
        elif self.stmt_seq_else is not None:
            self.stmt_seq_else.ExecStmtSeq(datapoints)