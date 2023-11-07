class Id:
    ids = []

    @staticmethod
    def ParseID1(tokenizer):
        name = tokenizer.idName()
        # Check to make sure the variable isn't declared already
        for id_dict in Id.ids:
            if name in id_dict:
                print("Parse Error: Variable already declared (" + name + ")")
                exit()
        # Declare the variable as uninitialized
        Id.ids.append({name: None})
        tokenizer.skipToken()

    def ParseID2(tokenizer):
        name = tokenizer.idName()
        is_declared = False
        # Check to make sure the variable isn't declared already
        for id_dict in Id.ids:
            if name in id_dict:
                is_declared = True
        # Declare the variable as uninitialized
        if not is_declared: 
            print("Parse Error: Variable not declared ("+name+")")
            exit()
        tokenizer.skipToken()

    @staticmethod
    def IdDeclared(name):
        # Check to make sure the variable isn't declared already
        for id_dict in Id.ids:
            if name in id_dict:
                return True

        return False


class IdList:
    def __init__(self, tokenizer, is_decl):
        self.tokenizer = tokenizer
        self.is_decl = is_decl
        self.id = None
        self.id_list = None

    def ParseIDList(self):
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected identifier, no ID specified")
            exit()
        if self.is_decl:
            self.id = self.tokenizer.idName()
            Id.ParseID1(self.tokenizer)
        else:
            self.id = self.tokenizer.idName()
            Id.ParseID2(self.tokenizer)

        # There is a comma separated list
        if self.tokenizer.getToken() == 13:
            # skip the comma
            self.tokenizer.skipToken()
            self.id_list = IdList(self.tokenizer, self.is_decl)
            self.id_list.ParseIDList()

    def PrintIdList(self, currentTab, inLine):
        print(self.id, end= ('' if inLine else '\n'))
        if self.id_list is not None:
            print(', ', end='')
            self.id_list.PrintIdList(0, inLine)
            
            
        