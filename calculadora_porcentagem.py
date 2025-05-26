from abc import ABC, abstractmethod

# Classe abstrata que define a estrutura de uma calculadora de porcentagem
class CalculadoraPorcentagem(ABC):
    @abstractmethod
    def calcular(self, parte, total):
        """
        Método abstrato para calcular a porcentagem.
        """
        pass

# Implementação simples que retorna o valor da porcentagem sem arredondar
class PorcentagemSimples(CalculadoraPorcentagem):
    def calcular(self, parte, total):
        if total == 0:
            raise ValueError("O total não pode ser zero.")
        return (parte / total) * 100

# Implementação que retorna a porcentagem arredondada com 2 casas decimais
class PorcentagemComArredondamento(CalculadoraPorcentagem):
    def calcular(self, parte, total):
        if total == 0:
            raise ValueError("O total não pode ser zero.")
        return round((parte / total) * 100, 2)

# Função adicional: calcula o valor da parte com base na porcentagem e no total
def calcular_parte(porcentagem, total):
    return (porcentagem / 100) * total

# Função adicional: calcula o valor total com base na parte e na porcentagem
def calcular_total(parte, porcentagem):
    if porcentagem == 0:
        raise ValueError("A porcentagem não pode ser zero.")
    return (parte * 100) / porcentagem

# Função adicional: calcula a diferença percentual entre dois valores
def diferenca_percentual(valor1, valor2):
    if valor1 == 0:
        raise ValueError("O primeiro valor não pode ser zero.")
    diferenca = valor2 - valor1
    return round((diferenca / valor1) * 100, 2)