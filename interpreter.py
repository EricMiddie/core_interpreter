# Eric Middlekamp
# 11/10/23
# CSE 3341

import sys
import os
from tokenizer import Tokenizer

# This class is not needed, but consolidates a lot of logic to keep main clean
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
            for line in file:
                try:
                    # Try to convert the line to an integer. Throw an error if it can't
                    integer_value = int(line.strip())
                    self.datapoints.append(integer_value)
                except ValueError:
                    print(f"Error: Ensure that your data is one integer value per line in {self.datastream}.")
                    exit()
        self.tokenizer = Tokenizer(filename=self.filename)

    def Parse(self):
        # Creates the program object and calls the Parse method
        from classes.prog import Prog
        self.program = Prog(self.tokenizer)
        self.program.ParseProg()
        self.tokenizer.close_file()
    def Print(self):
        # Pretty Prints the program
        self.program.PrintProg(0)
    def Exec(self):
        # Executes the program
        self.program.ExecProg(self.datapoints)

def main():
    if len(sys.argv) != 3:
        print("Incorrect command line arguments.")
        print("Usage: python <script_name>.py <filename>")
        exit()
        
    
    interp = Interpreter(filename=sys.argv[1], datastream=sys.argv[2])
    interp.Parse()
    interp.Print()
    interp.Exec()

if __name__ == "__main__":
    main()