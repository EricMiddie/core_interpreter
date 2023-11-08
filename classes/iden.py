class Id:
    __ids = {}
    @staticmethod
    def ParseID1(tokenizer):
        name = tokenizer.idName()
        # Check to make sure the variable isn't declared already
        if name in Id.__ids:
            print("Parse Error: Variable already declared (" + name + ")")
            exit()
        # Declare the variable as uninitialized
        Id.__ids[name] = None
        tokenizer.skipToken()

    @staticmethod
    def ParseID2(tokenizer):
        name = tokenizer.idName()
        # Check to make sure the variable isn't declared already
        is_declared =  name in Id.__ids
        # Declare the variable as uninitialized
        if not is_declared: 
            print("Parse Error: Variable not declared ("+name+")")
            exit()
        tokenizer.skipToken()

    @staticmethod
    def IdDeclared(name):
        # Check to make sure the variable isn't declared already
        return name in Id.__ids

    
    @staticmethod
    def ExecDeclId(name):
        # just verify that it's uninitialized
        # this is redundant from Parsing
        Id.__ids[name] = None

    @staticmethod
    def AssignIdValue(name, value):
        Id.__ids[name] = value

    @staticmethod
    def IdDefined(name):
        return False if Id.__ids[name] == None else True

    @staticmethod
    def GetIdValue(name):
        if not Id.IdDefined(name):
            print("Execution Error: Variable undefined ("+name+")")
            exit()
        return Id.__ids[name]
    
    def GetStringIdValue(name):
        return "undefined" if not Id.IdDefined(name) else str(Id.__ids[name])


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

    def ExecIdListDecl(self, datapoints):
        Id.ExecDeclId(self.id)

        if self.id_list is not None:
            self.id_list.ExecIdListDecl(datapoints)

    def ExecIdListIn(self, datapoints):
        if(len(datapoints) <= 0):
            print("Execution Error: Not enough input datapoints to assign to ids")
            exit()
        Id.AssignIdValue(self.id, datapoints[0])
        datapoints.pop(0)
        if self.id_list is not None:
            self.id_list.ExecIdListIn(datapoints)

    def ExecIdListOut(self, datapoints):
        print(f"{self.id} = {Id.GetStringIdValue(self.id)}")
        if self.id_list is not None:
            self.id_list.ExecIdListOut(datapoints)

            
            
        