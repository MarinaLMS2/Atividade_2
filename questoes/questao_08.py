class TorneioDeDrones:
    def __init__(self, nome_torneio, provas, bateria_inicial):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria_inicial
        self.pontos = 0
        self.provas_concluidas = []

    def listar_provas(self):
        for prova in self.provas:
            print(prova["nome"])

    def tentar_prova(self, numero_prova):
        indice = numero_prova - 1
        if indice >= 0 and indice < len(self.provas):
            prova = self.provas[indice]
            if self.bateria >= prova["custo"]:
                self.bateria -= prova["custo"]
                self.pontos += prova["pontuacao"]
                self.provas_concluidas.append(prova["nome"])

    def calcular_progresso(self):
        return len(self.provas_concluidas)

    def verificar_situacao(self):
        if len(self.provas_concluidas) == len(self.provas):
            return "Concluído"
        elif self.bateria == 0:
            return "Sem bateria"
        else:
            return "Em andamento"

    def exibir_relatorio(self):
        print(self.nome_torneio)
        print(self.bateria)
        print(self.pontos)
        print(self.verificar_situacao())


provas = [{"nome": "Corrida", "custo": 20, "pontuacao": 50}, {"nome": "Obstáculos", "custo": 30, "pontuacao": 80}]
t1 = TorneioDeDrones("Drone 1", provas, 100)
t1.tentar_prova(1)
t1.exibir_relatorio()

