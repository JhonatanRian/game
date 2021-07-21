from random import randint


class Calculus:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gera_valor
        self.__valor2: int = self._gera_valor
        self.__operacao: int = randint(1, 3) #1: adição; 2: subtração; 3: multiplicação
        self.__resultado: int = self._gera_resultado
        
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    def __str__(self: object) -> str:
        op = ""
        if self.operacao == 1:
            op = "somar"
        elif self.operacao == 2:
            op = "diminuir"
        elif self.operacao == 3:
            op = "multiplicar"
        else:
            op = "Operação desconhecida"
        
        return f"valor1: {self.valor1}\nvalor2: {self.valor2}\noperação: {self.operacao}\ndificuldade: {self.dificuldade}"
    
    @property
    def _gera_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 99999999)
    
    @property
    def _gera_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
        
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return 'x'
    
    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False
        
        if self.resultado == resposta:
            print("Resposta correta!")
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        
        return certo
    
    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')