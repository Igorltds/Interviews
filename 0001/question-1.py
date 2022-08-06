#questions-2
class Question_1():
    def __init__(self, indice=13):
        self.indice = indice
        self.soma = 0
        self.k = 0

    def calculate(self):
        while self.k < self.indice:
            self.k+=1
            self.soma = self.soma+self.k


'''
         Executando código:
'''

system = Question_1()
system.calculate()

print("\nResultado:", system.soma)