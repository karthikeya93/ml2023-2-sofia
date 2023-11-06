class helper:
    
    def __init__(self):
        self.n = None
        self.n_values = []
        self.x = None
    
    def askN(self):
        self.n = int(input('Hello, please enter a positive integer N'))
    
    def askNumbers(self):
        for i in range(self.n):
            self.n_values.append(int(input(f'Enter number {i+1}')))
        
    def showNumbers(self):
        for i in self.n_values:
            print(f'You entered {i}')
    
    def askANumber(self):
        self.x = int(input('Now enter an integer'))
        
    def finalResult(self):
        if self.x in self.n_values:
            print(self.n_values.index(self.x)+1)
        else:
            print(-1)
        

obj = helper()
obj.askN()
obj.askNumbers()
obj.showNumbers()
obj.askANumber()
obj.finalResult()
