class Decl:
    def __init__(self, id_list):
        self.id_list = id_list

    def ParseDecl(self):
         print("Parsing Declaration")
        


class DeclSeq:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decls = []

    def add_decl(self, decl):
        self.decls.append(decl)

    def ParseDeclSeq(self):
        # Make sure that it starts with an "int"
        if self.tokenizer.getToken() != 4:
                print("Error: Expected int to start declaration sequence")
