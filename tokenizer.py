# Eric Middlekamp
# CSE 3341
# 10/6/23

import sys
import os

TOKENS = {
    "PROGRAM": (1, "program"),
    "BEGIN": (2, "begin"),
    "END": (3, "end"),
    "INT": (4, "int"),
    "IF": (5, "if"),
    "THEN": (6, "then"),
    "ELSE": (7, "else"),
    "WHILE": (8, "while"),
    "LOOP": (9, "loop"),
    "READ": (10, "read"),
    "WRITE": (11, "write"),
    "SEMICOLON": (12, ";"),
    "COMMA": (13, ","),
    "EQUALS": (14, "="),
    "EXCLAMATION": (15, "!"),
    "OPEN_BRACKET": (16, "["),
    "CLOSE_BRACKET": (17, "]"),
    "AND": (18, "&&"),
    "OR": (19, "||"),
    "OPEN_PAREN": (20, "("),
    "CLOSE_PAREN": (21, ")"),
    "PLUS": (22, "+"),
    "MINUS": (23, "-"),
    "MULTIPLY": (24, "*"),
    "NOT_EQUALS": (25, "!="),
    "DOUBLE_EQUALS": (26, "=="),
    "LESS_THAN": (27, "<"),
    "GREATER_THAN": (28, ">"),
    "LESS_THAN_EQUALS": (29, "<="),
    "GREATER_THAN_EQUALS": (30, ">="),
    # "INTEGER": (31)
    # "IDENTIFIER": (32)
}

class Tokenizer:
    
    def __init__(self, filename):
        self.filename = filename
        self.tokens = []
        self.cursor_index = 0
        self.file = open(self.filename, 'r')
        self.tokenizeLine()

    def tokenizeLine(self):
        line = self.file.readline()
        # End of the file
        if not line:
            return

        # Remove white space and setup the index
        line = line.strip()
        index = 0

        if len(line) == 0:
            return self.tokenizeLine()

        while index < len(line):
            # Separate out the characters of the next token
            substring = line[index:]
            matched = False
            og_substring = substring
            substring = substring.lstrip()
            # Offset the index based on the amount of white space removed
            index += len(og_substring) - len(substring)

            # Check the reserved words, or if it's an identifier
            if substring[0].isalpha():
                end_index = index + 1
                while end_index < len(line) and (line[end_index].isalpha() or line[end_index].isdigit()):
                    end_index += 1
                token_str = line[index:end_index]


                # Checking reserved words
                for token_name, (token_num, pattern) in TOKENS.items():
                    if pattern == token_str:
                        self.tokens.append((token_num, token_str))
                        matched = True
                        break

                # Checking if it meets criteria for identifier
                if not matched:
                    if (token_str.isupper() and (len(token_str)) == 1 or (token_str[1:].isalnum() and token_str[0:].isupper() and token_str[0].isalpha())):
                        self.tokens.append((32, token_str))
                        matched = True

                index = end_index - 1

            # Checks Integer criteria
            elif substring[0].isdigit():
                end_index = index + 1
                while end_index < len(line) and line[end_index].isdigit():
                    end_index += 1
                token_str = line[index:end_index]

                if end_index < len(line) and line[end_index].isalnum():
                    self.tokens.append((34, "Error: Illegal token detected in line - " + line))
                    break

                if token_str == '0' or (token_str[0] != '0' and token_str.isdigit()):
                    self.tokens.append((31, token_str))
                    matched = True
                    index = end_index - 1

            # Check if it matches a special symbol
            else:
                matched_tokens = []

                # Create a list of all matching special symbol
                for token_name, (token_num, pattern) in TOKENS.items():
                    if substring.startswith(pattern):
                        matched_tokens.append((token_num, pattern))
                
                # If there is >= 1 that matches, take the biggest.
                if matched_tokens:
                    matched_tokens.sort(key=lambda x: len(x[1]), reverse=True)
                    token_num, pattern = matched_tokens[0]
                    self.tokens.append((token_num, pattern))
                    matched = True
                    index += len(pattern) - 1

            # If no match found, add an error token with the line it failed to parse
            if not matched:
                self.tokens.append((34, "Error: Illegal token detected in line - " + line))
                break

            index += 1


    def getToken(self):
        # Check that it's not EOF, then return the token
        if self.cursor_index >= len(self.tokens):
            return 33
        return self.tokens[self.cursor_index][0]

    def skipToken(self):
        # Increment the cursor if there are more tokens
        if self.cursor_index < len(self.tokens):
            self.cursor_index += 1

        # Get the next line of tokens if not
        if self.cursor_index == len(self.tokens):
            self.tokenizeLine()

    def intVal(self):
        token_type, token_value = self.tokens[self.cursor_index]
        if token_type != 31:
            print("Error: Current token is not an integer.")
            exit()
        return int(token_value)

    def idName(self):
        token_type, token_value = self.tokens[self.cursor_index]
        if token_type != 32:
            print("Error: Current token is not an identifier.")
            exit()
        return token_value
    
    def get_error(self):
        token_type, token_value = self.tokens[self.cursor_index]
        if token_type != 34:
            print("Error: Current token is not an error.")
            exit()
        return token_value

def main():
    if len(sys.argv) != 2:
        print("Incorrect command line arguments.")
        print("Usage: python <script_name>.py <filename>")
        exit()

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Error: '{filename}' is not a valid file path")
        exit()

    print(f"Tokenizing file: {filename}")
    tokenizer = Tokenizer(filename)

    while True:
        token = tokenizer.getToken()
        print(token)
        if token in [33, 34]:
            if token == 34:
                print(tokenizer.get_error())
            else:
                print("End of file reached.")
            break
        tokenizer.skipToken()

    tokenizer.file.close()

if __name__ == "__main__":
    main()
