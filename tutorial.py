class _Private:
    def __init__(self,name):
        self.name=name

class NotPrivate:
    def __init__(self,name) :
          self.name= name 
          self.priv = _Private(name)
    
    def display(self):
         print('hello')
    
    def display(self):
         print('hi')