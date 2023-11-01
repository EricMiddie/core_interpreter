from classes.iden import IdList

class Decl:
    def __init__(self, tokenizer):
        self.id_list = None
        self.tokenizer = tokenizer

    def ParseDecl(self):
        print("Parsing Declaration")
        self.id_list = IdList(tokenizer=self.tokenizer)
        # check and skip the "int"
        if self.tokenizer.getToken() != 4:
            print("Error: expected int at start of declaration")
            exit()
        self.tokenizer.skipToken()

        # parse the ID List
        self.id_list.ParseIDList()

        # check and skip the ;
        if self.tokenizer.getToken() != 12:
            print("Error: Expected ; after ID list")
            exit()
        self.tokenizer.skipToken()
         
        


class DeclSeq:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decls = []


    def ParseDeclSeq(self):
        print("Parsing Declaration Sequence")
        initDecl = Decl(self.tokenizer)
        # Make sure that it starts with an "int"
        if self.tokenizer.getToken() != 4:
                print("Error: Expected int to start declaration sequence")
                exit()
        self.decls.append(initDecl)
        initDecl.ParseDecl()
        while self.tokenizer.getToken() == 4:
            initDecl = Decl(self.tokenizer)
            self.decls.append(initDecl)
            initDecl.ParseDecl()

