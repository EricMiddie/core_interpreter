from classes.op import Op
from classes.compop import CompOp

class Comp:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.left_op = None
        self.comp_op = None
        self.right_op = None

    def ParseComp(self):
        self.left_op = Op(self.tokenizer)
        self.comp_op = CompOp(self.tokenizer)
        self.right_op = Op(self.tokenizer)
        #check and skip the (
        if self.tokenizer.getToken() != 20:
            print("Parse Error: Comparator expected to start with (")
            exit()
        self.tokenizer.skipToken()

        # Parse the left_op, comp_op, and right_op
        self.left_op.ParseOp()
        self.comp_op.ParseCompOp()
        self.right_op.ParseOp()

        # check for and skip the )
        if self.tokenizer.getToken() != 21:
            print("Parse Error: Expected closing )")
            exit()
        self.tokenizer.skipToken()