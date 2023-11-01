class Id:
    def __init__(self, name, value, tokenizer):
        # As defined by RE, we'll keep it simple and just store the value.
        self.name = name
        self.value = value
        self.tokenizer = tokenizer
    
    def ParseID(self):
        print("")

class IdList:
    def __init__(self, tokenizer):
        self.ids = []
        self.tokenizer = tokenizer

    def add_id(self, id):
        self.ids.append(id)

    def ParseIDList(self):
        if self.tokenizer.getToken() != 32:
            print("Expected identifier, no IDs specified")
        while(self.tokenizer.getToken() != 32):
            name = self.tokenizer.idName()
            
            
        