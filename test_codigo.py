import unittest
from codigo_refatorado import PorcentagemSimples, PorcentagemComArredondamento

class TestPorcentagem(unittest.TestCase):
    def test_porcentagem_simples(self):
        p = PorcentagemSimples()
        self.assertEqual(p.calcular(50, 200), 25.0)

    def test_porcentagem_arredondada(self):
        p = PorcentagemComArredondamento()
        self.assertEqual(p.calcular(30, 150), 20.0)

    def test_divisao_por_zero(self):
        p = PorcentagemSimples()
        with self.assertRaises(ValueError):
            p.calcular(10, 0)

if __name__ == "__main__":
    unittest.main()
