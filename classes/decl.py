from classes.iden import IdList

class Decl:
    def __init__(self, tokenizer):
        self.id_list = None
        self.tokenizer = tokenizer

    def ParseDecl(self):
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
        # Print the Id list in line
        tabs = '\t' * currentTab
        print(f"{tabs}int", end=' ')
        self.id_list.PrintIdList(0, True)
        print(";")

    def ExecDecl(self, datapoints):
        # Call the specific ID list execution functino (decl in this case)
        self.id_list.ExecIdListDecl(datapoints)

         
        


class DeclSeq:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decl = None
        self.decl_seq = None


    def ParseDeclSeq(self):
        self.decl = Decl(self.tokenizer)
        # Make sure that it starts with an "int"
        if self.tokenizer.getToken() != 4:
                print("Error: Expected int to start declaration sequence")
                exit()
        # Parse that decl
        self.decl.ParseDecl()
        if self.tokenizer.getToken() == 4:
            # See if there is another Decl Seq to parse
            self.decl_seq = DeclSeq(self.tokenizer)
            self.decl_seq.ParseDeclSeq()

    def PrintDeclSeq(self, currentTab):
        # Print the decl and see if there is another decl deq to print
        self.decl.PrintDecl(currentTab)
        if self.decl_seq is not None:
            self.decl_seq.PrintDeclSeq(currentTab)

    def ExecDeclSeq(self, datapoints):
        # Execute the decl and then see if there is another decl seq to execute
        self.decl.ExecDecl(datapoints)
        if self.decl_seq is not None:
            self.decl_seq.ExecDeclSeq(datapoints)

