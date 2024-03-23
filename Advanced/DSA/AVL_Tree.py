class AVL_Tree:

    def __init__(self, Value = None):

        self.Value = Value
        self.Height = 0

        if self.Value:

            self.Left = AVL_Tree()
            self.Right = AVL_Tree()
            self.Height = 1

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

            return []
        
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
            self.Left = AVL_Tree()
            self.Right = AVL_Tree()
            self.Height = 1 + max(self.Left.Height, self.Right.Height)

            self.Rebalance()

        if (self.Value==Value):
            
            return
        
        if (Value<self.Value):
            
            self.Left.Insert(Value)
            self.Rebalance()

            self.Height = 1 + max(self.Left.Height, self.Right.Height)

            return

        else:
            
            self.Right.Insert(Value)
            self.Rebalance()

            self.Height = 1 + max(self.Left.Height, self.Right.Height)

            return
        
    
    def Delete(self, Value):

        if (self.isempty()):

            return
        
        if (Value<self.Value):

            self.Left.Delete(Value)
            self.Rebalance()

            self.Height = 1 + max(self.Left.Height, self.Right.Height)

            return
        
        if (Value>self.Value):

            self.Right.Delete(Value)
            self.Rebalance()

            self.Height = 1 + max(self.Left.Height, self.Right.Height)

            return
        
        if (self.Value==Value):

            if (self.isleaf()):

                self.Make_Empty()

            elif (self.Left.isempty()):

                self.Copy_Right()

            elif (self.Right.isempty()):

                self.Copy_Left()

            else:

                Var = self.Left.Maximum()
                
                self.Value = Var
                self.Left.Delete(Var)

            return


    def Left_Rotate(self):

        Value = self.Value
        Value_Right = self.Right.Value

        Tree_Left = self.Left
        Tree_Right_Left = self.Right.Left
        Tree_Right_Right = self.Right.Right

        New_Left = AVL_Tree(Value)
        New_Left.Left = Tree_Left
        New_Left.Right = Tree_Right_Left

        self.Value = Value_Right
        self.Right = Tree_Right_Right
        self.Left = New_Left

        New_Left.Height = 1 + max(New_Left.Left.Height, New_Left.Right.Height)
        self.Height = 1 + max(self.Left.Height, self.Right.Height)

        return
    

    def Right_Rotate(self):


        Value = self.Value
        Value_Left = self.Left.Value

        Tree_Left_Left = self.Left.Left
        Tree_Left_Right = self.Left.Right
        Tree_Right = self.Right

        New_Right = AVL_Tree(Value)
        New_Right.Left = Tree_Left_Right
        New_Right.Right = Tree_Right

        self.Value = Value_Left
        self.Left = Tree_Left_Left
        self.Right = New_Right

        New_Right.Height = 1 + max(New_Right.Left.Height, New_Right.Right.Height)
        self.Height = 1 + max(self.Left.Height, self.Right.Height)

        return
            

    def Rebalance(self):

        Current_Slope = self.Left.Height - self.Right.Height

        if (Current_Slope==2):

            Tree_Left = self.Left
            Slope_Left = Tree_Left.Left.Height - Tree_Left.Right.Height

            if (Slope_Left==0 or Slope_Left==1):

                self.Right_Rotate()

                return
            
            else:

                Tree_Left.Left_Rotate()
                self.Right_Rotate()

                return
            
        if (Current_Slope==-2):

            Tree_Right = self.Right
            Slope_Right = Tree_Right.Left.Height - Tree_Right.Right.Height

            if (Slope_Right==0 or Slope_Right==1):

                Tree_Right.Right_Rotate()
                self.Left_Rotate()

                return
            
            else:

                self.Left_Rotate()

                return
            
        return


    def isempty(self):

        return self.Value == None
    
    
    def isleaf(self):

        return self.Value != None and self.Right.isempty() and self.Right.isempty()
    

    def Make_Empty(self):

        self.Value = None
        self.Height = 0
        self.Left = None
        self.Right = None

        return
    

    def Copy_Left(self):

        self.Value = self.Left.Value
        self.Height = self.Left.Height
        self.Right = self.Left.Right
        self.Left = self.Left.Left

        return
    

    def Copy_Right(self):

        self.Value = self.Right.Value
        self.Height = self.Right.Height
        self.Left = self.Right.Left
        self.Right = self.Right.Right

        return
    

    def __str__(self):

        return str(self.Inorder())


if __name__ == "__main__":

    Tree = AVL_Tree(5)
    Tree.Insert(3)
    Tree.Insert(6)
    Tree.Insert(2)
    Tree.Insert(4)
    Tree.Insert(7)
    Tree.Insert(1)

    print(Tree.Pre_Order())