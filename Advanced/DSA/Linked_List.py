class Node:

    def __init__(self, Value=None):

        self.Value=Value
        self.Next=None

        return

    def isempty(self):

        if self.Value==None:

            return True
        
        return False
    
    def append(self, Value):

        if self.isempty():

            self.Value=Value

        elif self.Next==None:

            self.Next=Node(Value)

        else:

            self.next.append(Value)

        return
    
    def insert(self, Value):

        if self.isempty():

            self.Value=Value

            return
        
        New_Node=Node(Value)

        self.Value, New_Node.Value = New_Node.Value, self.Value
        self.Next, New_Node.Next = New_Node.Next, self.Next

        return
    
    def delete(self, Value):

        if self.isempty():

            return
        
        elif self.Value==Value:

            self.Value=None

            if self.Next!=None:

                self.Value=self.Next.Value
                self.Next=self.Next.Next

        else:

            if self.Next!=None:

                self.Next.delete(Value)

                if self.Next.Value==None:

                    self.Next=None

        return