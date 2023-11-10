from classes.iden import IdList

class In:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.id_list = None

    def ParseIn(self):
        # Check and skip 'read'
        if(self.tokenizer.getToken() != 10):
            print("Parse Error: Expected 'read' to start IN statement.")
            exit()
        self.tokenizer.skipToken()
        # Create the id list and parse it
        self.id_list = IdList(self.tokenizer, False)
        self.id_list.ParseIDList()

        # Check and skip ';'
        if(self.tokenizer.getToken() != 12):
            print("Parse Error: Expected IN to end with ;")
            exit()
        self.tokenizer.skipToken()

    def PrintIn(self, currentTab):
        # Print the read at the current tab
        tabs = '\t' * currentTab
        print(f"{tabs}read ", end='')
        # Print the ID list inline
        self.id_list.PrintIdList(currentTab, True)
        print(';')

    def ExecIn(self, datapoints):
        # Execute the id list input
        self.id_list.ExecIdListIn(datapoints)

class Out:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.id_list = None

    def ParseOut(self):
        # Check and skip the 'write' token
        if(self.tokenizer.getToken() != 11):
            print("Parse Error: Expected 'write' to start OUT statement.")
            exit()
        self.tokenizer.skipToken()
        # Init the ID list and parse it
        self.id_list = IdList(self.tokenizer, False)
        self.id_list.ParseIDList()

        # Check and skip ';'
        if(self.tokenizer.getToken() != 12):
            print("Parse Error: Expected OUT to end with ;")
            exit()
        self.tokenizer.skipToken()

    def PrintOut(self, currentTab):
        # print the write statement inline at the current tab
        tabs = '\t' * currentTab
        print(f"{tabs}write ", end='')
        # print the ID list in line
        self.id_list.PrintIdList(currentTab, True)
        print(';')

    def ExecOut(self, datapoints):
        # Execute the output for the id list
        self.id_list.ExecIdListOut(datapoints)