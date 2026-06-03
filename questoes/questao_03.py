class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima

    def adicionar_amostra(self, amostra):
        if amostra != '' and len(self.amostras) < self.capacidade_maxima:
            self.amostras.append(amostra)
            print("Amostra adicionada.")
        else:
            print("Nao foi possivel adicionar.")

    def listar_amostras(self):
        print("Amostras coletadas:")
        for amostra in self.amostras:
            print(amostra)

    def contar_amostras(self):
        return len(self.amostras)

    def verificar_armazenamento(self):
        if len(self.amostras) >= self.capacidade_maxima:
            return "Armazenamento cheio"
        else:
            return "Ainda tem espaco"

    def exibir_relatorio(self):
        print(f"Robo: {self.nome}")
        print(f"Quantidade de amostras: {self.contar_amostras()}")
        print(f"Capacidade: {self.capacidade_maxima}")
        print(f"Situacao: {self.verificar_armazenamento()}")


p1 = RoboColetor("MMMMM", [], 3)
p1.adicionar_amostra("Rocha")
p1.adicionar_amostra("Cristal")
p1.listar_amostras()
p1.exibir_relatorio()
