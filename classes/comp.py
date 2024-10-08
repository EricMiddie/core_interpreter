from classes.op import Op
from classes.compop import CompOp

class Comp:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.left_op = None
        self.comp_op = None
        self.right_op = None

    def ParseComp(self):
        # initialize the objects for the children of the class
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

    def PrintComp(self):
        # Print the values and children in line
        print("(", end='')
        self.left_op.PrintOp(0, True)
        self.comp_op.PrintCompOp(0)
        self.right_op.PrintOp(0, True)
        print(")", end='')

    def EvalComp(self, datapoints):
        # get the values of the left and right
        leftVal = self.left_op.EvalOp(datapoints)
        rightVal = self.right_op.EvalOp(datapoints)

        # Call EvalComp which just returns the token of the compop
        comp = self.comp_op.EvalCompOp()

        # Check the comp op and do the expected operation
        if comp == 25:
            return leftVal != rightVal
        elif comp == 26:
            return leftVal == rightVal
        elif comp == 27:
            return leftVal < rightVal
        elif comp == 28:
            return leftVal > rightVal
        elif comp == 29:
            return leftVal <= rightVal
        elif comp == 30:
            return leftVal >= rightVal
        else:
            # Should never hit this
            print("Execution Error: Invalid Comparator provided")
            print(comp)
            exit()
        