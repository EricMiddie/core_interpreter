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
        # Assign the value to the dictionary
        Id.__ids[name] = value

    @staticmethod
    def IdDefined(name):
        # Check that the value is not None
        return False if Id.__ids[name] == None else True

    @staticmethod
    def GetIdValue(name):
        # Make sure that the ID is defined before getting the value
        if not Id.IdDefined(name):
            print("Execution Error: Variable undefined ("+name+")")
            exit()
        return Id.__ids[name]
    
    def GetStringIdValue(name):
        # This allows you to print undefined variables, but you can't use them in operations
        return "undefined" if not Id.IdDefined(name) else str(Id.__ids[name])


class IdList:
    def __init__(self, tokenizer, is_decl):
        self.tokenizer = tokenizer
        self.is_decl = is_decl
        self.id = None
        self.id_list = None

    def ParseIDList(self):
        # Make sure that you're on an ID
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected identifier, no ID specified")
            exit()
        # Check that it's a declaration so we know what ParseId to call
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
        # Print the id list in line
        print(self.id, end= ('' if inLine else '\n'))
        if self.id_list is not None:
            print(', ', end='')
            self.id_list.PrintIdList(0, inLine)

    def ExecIdListDecl(self, datapoints):
        #Execute the ID for declarations
        Id.ExecDeclId(self.id)

        # Check if there is another ID list to declare
        if self.id_list is not None:
            self.id_list.ExecIdListDecl(datapoints)

    def ExecIdListIn(self, datapoints):
        # Make sure that there are datapoints to assign, throw error if not.
        if(len(datapoints) <= 0):
            print(f"Execution Error: Not enough input datapoints to assign to id ({self.id})")
            exit()
        # Assign the first data point to the id and remove the data point
        Id.AssignIdValue(self.id, datapoints[0])
        datapoints.pop(0)
        # If there are more Ids, assign those too
        if self.id_list is not None:
            self.id_list.ExecIdListIn(datapoints)

    def ExecIdListOut(self, datapoints):
        # Print the id
        print(f"{self.id} = {Id.GetStringIdValue(self.id)}")
        # Print the remaining Id list
        if self.id_list is not None:
            self.id_list.ExecIdListOut(datapoints)

            
            
        