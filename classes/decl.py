from classes.iden import IdList

class Decl:
    def __init__(self, tokenizer):
        self.id_list = None
        self.tokenizer = tokenizer

    def ParseDecl(self):
        # print("Parsing Declaration")
        self.id_list = IdList(self.tokenizer, True)
        # check and skip the "int"
        if self.tokenizer.getToken() != 4:
            print("Error: expected int at start of declaration")
            exit()
        self.tokenizer.skipToken()

        # parse the ID List
        self.id_list.ParseIDList()

        # check and skip the ;
        if self.tokenizer.getToken() != 12:
            print("Parse Error: Expected ; after ID list")
            exit()
        self.tokenizer.skipToken()

    def PrintDecl(self, currentTab):
        tabs = '\t' * currentTab
        print(f"{tabs}int", end=' ')
        self.id_list.PrintIdList(0, True)
        print(";")

    def ExecDecl(self, datapoints):
        self.id_list.ExecIdListDecl(datapoints)

         
        


class DeclSeq:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decl = None
        self.decl_seq = None


    def ParseDeclSeq(self):
        # print("Parsing Declaration Sequence")
        self.decl = Decl(self.tokenizer)
        # Make sure that it starts with an "int"
        if self.tokenizer.getToken() != 4:
                print("Error: Expected int to start declaration sequence")
                exit()
        self.decl.ParseDecl()
        if self.tokenizer.getToken() == 4:
            self.decl_seq = DeclSeq(self.tokenizer)
            self.decl_seq.ParseDeclSeq()

    def PrintDeclSeq(self, currentTab):
        self.decl.PrintDecl(currentTab)
        if self.decl_seq is not None:
            self.decl_seq.PrintDeclSeq(currentTab)

    def ExecDeclSeq(self, datapoints):
        self.decl.ExecDecl(datapoints)
        if self.decl_seq is not None:
            self.decl_seq.ExecDeclSeq(datapoints)

