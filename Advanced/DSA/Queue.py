class Queue:

    def __init__(self):

        self.queue=[]

    def Put(self, Value):

        self.queue.append(Value)

    def Get(self):

        Value=None

        if not self.isempty():

            Value=self.queue[0]
            self.queue=self.queue[1:]

        return Value
    
    def isempty(self):

        return (self.queue==[])
    
    def __str__(self):

        return str(self.queue)