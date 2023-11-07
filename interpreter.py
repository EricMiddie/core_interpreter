import sys
import os
from tokenizer import Tokenizer

class Interpreter:

    def __init__(self, filename, datastream):
        self.filename = filename
        self.datastream = datastream
        self.program = None
        self.tokenizer = None
        self.datapoints = []
        self.setup()

    def setup(self):
        # Validates the users input files
        if not os.path.exists(self.filename):
            print(f"Error: '{self.filename}' is not a valid file path")
            exit()

        if not os.path.exists(self.datastream):
            print(f"Error: '{self.datastream}' is not a valid file path")
            exit()

        # reads the datastream into the interpreter
        with open(self.datastream, 'r') as file:
            lines = file.readlines()
        self.datapoints = [line.strip() for line in lines]

        print("Init Tokenizer")
        self.tokenizer = Tokenizer(filename=self.filename)

    def Parse(self):
        from classes.prog import Prog
        self.program = Prog(self.tokenizer)
        self.program.ParseProg()
        print("Program Parsed")
    def Print(self):
        self.program.PrintProg(0)
        print("Not implemented")
    def Exec(self):
        print("Not implemented")
        

def main():
    if len(sys.argv) != 3:
        print("Incorrect command line arguments.")
        print("Usage: python <script_name>.py <filename>")
        exit()

    filename = sys.argv[1]
    datastream = sys.argv[2]

    if not os.path.exists(filename):
        print(f"Error: '{filename}' is not a valid file path")
        exit()

    if not os.path.exists(datastream):
        print(f"Error: '{datastream}' is not a valid file path")
        exit()

    interp = Interpreter(filename=filename, datastream=datastream)
    interp.Parse()
    interp.Print()

if __name__ == "__main__":
    main()