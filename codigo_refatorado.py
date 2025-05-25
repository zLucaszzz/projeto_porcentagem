from abc import ABC, abstractmethod

class CalculadoraPorcentagem(ABC):
    @abstractmethod
    def calcular(self, parte, total):
        pass

class PorcentagemSimples(CalculadoraPorcentagem):
    def calcular(self, parte, total):
        if total == 0:
            raise ValueError("O total não pode ser zero.")
        return (parte / total) * 100

class PorcentagemComArredondamento(CalculadoraPorcentagem):
    def calcular(self, parte, total):
        if total == 0:
            raise ValueError("O total não pode ser zero.")
        return round((parte / total) * 100, 2)

if __name__ == "__main__":
    simples = PorcentagemSimples()
    arredondado = PorcentagemComArredondamento()

    print("Porcentagem Simples:", simples.calcular(50, 200))
    print("Porcentagem Arredondada:", arredondado.calcular(30, 150))
