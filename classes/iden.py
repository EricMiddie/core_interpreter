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

    def ParseIDList(self):
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected identifier, no IDs specified")
            exit()
        if self.is_decl:
            Id.ParseID1(self.tokenizer)
        else:
            Id.ParseID2(self.tokenizer)

        # repeat while there is still a comma separated list
        while(self.tokenizer.getToken() == 13):
            self.tokenizer.skipToken()
            if self.tokenizer.getToken() != 32:
                print("Parse Error: Expected identifier after comma")
                exit()
            # skip the comma
            if self.is_decl:
                Id.ParseID1(self.tokenizer)
            else:
                Id.ParseID2(self.tokenizer)
            
            
        