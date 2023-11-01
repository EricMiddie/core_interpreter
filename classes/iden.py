class Id:
    ids = []

    @staticmethod
    def ParseID(tokenizer):
        name = tokenizer.idName()
        # Check to make sure the variable isn't declared already
        for id_dict in Id.ids:
            if name in id_dict:
                print("Parse Error: Variable already declared (" + name + ")")
                exit()
        # Declare the variable as uninitialized
        Id.ids.append({name: None})
        tokenizer.skipToken()


class IdList:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def ParseIDList(self):
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected identifier, no IDs specified")
            exit()

        Id.ParseID(tokenizer=self.tokenizer)

        # repeat while there is still a comma separated list
        while(self.tokenizer.getToken() == 13):
            self.tokenizer.skipToken()
            if self.tokenizer.getToken() != 32:
                print("Parse Error: Expected identifier after comma")
                exit()
            # skip the comma
            Id.ParseID(tokenizer=self.tokenizer)
            
            
        