class Tree:

    def __init__(self, Value = None):

        self.Value = Value

        if self.Value:

            self.Left = Tree()
            self.Right = Tree()

        else:

            self.Left = None
            self.Right = None

        return
        

    def In_Order(self):

        if (self.isempty()):

            return []
        
        else:

            return self.Left.In_Order() + [self.Value] + self.Right.In_Order()
        

    def Pre_Order(self):

        if (self.isempty()):

            return [None]
        
        else:

            return [self.Value] + self.Left.Pre_Order() +  self.Right.Pre_Order()


    def Post_Order(self):

        if (self.isempty()):

            return []
        
        else:

            return self.Left.Pre_Order() +  self.Right.Pre_Order() + [self.Value]
        

    def Search(self, Value):

        if (self.isempty()):

            return False
        
        if (self.Value==Value):

            return True
        
        if (Value<self.Value):

            return self.Left.Search(Value)
        
        if (Value>self.Value):

            return self.Right.Search(Value)
        

    def Minimum(self):

        if (self.Left.isempty()):

            return self.Value
        
        return self.Left.Minimum()
    

    def Maximum(self):

        if (self.Right.isempty()):

            return self.Value
        
        return self.Right.Maximum()
    

    def Insert(self, Value):

        if (self.isempty()):

            self.Value = Value
            self.Left = Tree()
            self.Right = Tree()

        if (self.Value==Value):
            
            return
        
        if (Value<self.Value):
            
            self.Left.Insert(Value)

            return

        else:
            
            self.Right.Insert(Value)

            return
        
    
    def Delete(self, Value):

        if (self.isempty()):

            return
        
        if (Value<self.Value):

            self.Left.Delete(Value)

            return
        
        if (Value>self.Value):

            self.Right.Delete(Value)

            return
        
        if (self.Value==Value):

            if (self.isleaf()):

                self.Make_Empty()

            elif (self.Left.isempty()):

                self.Copy_Right()

            elif (self.Right.isempty()):

                self.Copy_Left()

            else:

                Var=self.Left.Maximum()
                
                self.Value=Var
                self.Left.Delete(Var)

            return


    def isempty(self):

        return self.Value == None
    
    
    def isleaf(self):

        return self.Value != None and self.Right.isempty() and self.Right.isempty()
    

    def Make_Empty(self):

        self.Value = None

        self.Left = None
        self.Right = None

        return
    

    def Copy_Left(self):

        self.Value = self.Left.Value

        self.Right = self.Left.Right
        self.Left = self.Left.Left

        return
    

    def Copy_Right(self):

        self.Value = self.Right.Value
        
        self.Left = self.Right.Left
        self.Right = self.Right.Right

        return
    

    def __str__(self):

        return str(self.Inorder())