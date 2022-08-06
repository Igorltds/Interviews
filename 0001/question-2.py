#questions-2

class Fibonacci():
    def __init__(self, x, y):
        self.list = [x, y]
    
    def calculate(self, numb):
        for n in range(0, numb):
            x = int(self.list[-2])
            y = int(self.list[-1])
            z = x+y
            self.list.append(z)
        
    def iffind(self, setem):
        for item in self.list:
            if setem == item: return True
        return False


'''
         Executando código:
'''

#informando os dois primeiros digitos fibonacci
system = Fibonacci(0,1)
#mostrar lista
print("\nLista inicial:", system.list)

#criando os próximos x numeros da lista
system.calculate(10) 

#prints
print("\nLista, Atualização:", system.list)
print("Encontrado 88: ", system.iffind(88))
print("Encontrado 89: ", system.iffind(89))