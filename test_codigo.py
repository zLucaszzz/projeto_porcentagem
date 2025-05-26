import unittest
from calculadora_porcentagem import (
    PorcentagemSimples,
    PorcentagemComArredondamento,
    calcular_parte,
    calcular_total,
    diferenca_percentual
)

class TestPorcentagem(unittest.TestCase):

    def test_porcentagem_simples(self):
        p = PorcentagemSimples()
        resultado = p.calcular(50, 200)
        self.assertEqual(resultado, 25.0)

    def test_porcentagem_arredondada(self):
        p = PorcentagemComArredondamento()
        resultado = p.calcular(30, 150)
        self.assertEqual(resultado, 20.0)

    def test_divisao_por_zero_simples(self):
        p = PorcentagemSimples()
        with self.assertRaises(ValueError):
            p.calcular(10, 0)

    def test_divisao_por_zero_arredondado(self):
        p = PorcentagemComArredondamento()
        with self.assertRaises(ValueError):
            p.calcular(10, 0)

class TestFuncoesAdicionais(unittest.TestCase):

    def test_calcular_parte(self):
        resultado = calcular_parte(25, 200)
        self.assertEqual(resultado, 50)

    def test_calcular_total(self):
        resultado = calcular_total(50, 25)
        self.assertEqual(resultado, 200)

    def test_calcular_total_zero_porcentagem(self):
        with self.assertRaises(ValueError):
            calcular_total(50, 0)

    def test_diferenca_percentual(self):
        resultado = diferenca_percentual(100, 150)
        self.assertEqual(resultado, 50.0)

    def test_diferenca_percentual_negativa(self):
        resultado = diferenca_percentual(200, 150)
        self.assertEqual(resultado, -25.0)

    def test_diferenca_percentual_zero_valor1(self):
        with self.assertRaises(ValueError):
            diferenca_percentual(0, 150)

if __name__ == "__main__":
    unittest.main()
