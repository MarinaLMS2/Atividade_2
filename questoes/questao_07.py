class ExpedicaoTemplo:
    def __init__(self, nome_expedicao, desafios, energia_inicial):
        self.nome_expedicao = nome_expedicao
        self.desafios = desafios
        self.energia = energia_inicial
        self.pontos = 0
        self.desafios_concluidos = []

    def listar_desafios(self):
        for desafio in self.desafios:
            print(desafio["nome"])

    def tentar_desafio(self, numero):
        if numero < 1 or numero > len(self.desafios):
            print("Desafio inválido")
            return

        desafio = self.desafios[numero - 1]

        if self.energia >= desafio["custo"]:
            self.energia -= desafio["custo"]
            self.pontos += desafio["energia"]
            self.desafios_concluidos.append(desafio["nome"])

    def calcular_progresso(self):
        return len(self.desafios_concluidos)

    def verificar_situacao(self):
        if len(self.desafios_concluidos) == len(self.desafios):
            return "Concluida"
        elif self.energia == 0:
            return "Sem energia"
        else:
            return "Em andamento"

    def exibir_relatorio(self):
        print("Expedicao:", self.nome_expedicao)
        print("Energia:", self.energia)
        print("Pontos:", self.pontos)
        print("Situacao:", self.verificar_situacao())

desafios = [
    {"nome": "Sala 1", "custo": 20, "energia": 50},
    {"nome": "Sala 2", "custo": 30, "energia": 70}
]
p1 = ExpedicaoTemplo("MMMMMMM", desafios, 100)
p1.tentar_desafio(1)
p1.exibir_relatorio()