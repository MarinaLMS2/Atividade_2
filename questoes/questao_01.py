class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura =ano_abertura
        self.ano_atual =ano_atual

    def pode_abrir(self):
        if self.ano_atual >= self.ano_abertura:
            print("capsual pode ser aberta!")
        else:
            print("capsula n pode ser aberta!")

    def calcular_espera(self):
        return self.ano_abertura - self.ano_atual

    def classificar_espera(self):
        if self.calcular_espera() <= 0:
            print("Pode abrir agoraaa!!")
        elif self.calcular_espera() <= 3:
            print("Espera curta.")
        else:
            print("Espera longaaaaa!!!")

    def exibir_resumo(self):
        print(F"Autor:,{self.autor}\n"
              F"Ano de Abertura:{self.ano_abertura}\n"
              F"Situacao da capsula:{self.calcular_espera()}")

p1 = CapsulaDoTempo("Marina", "oiii mundo", 34, 36)

p1.pode_abrir()
print(p1.calcular_espera())
p1.classificar_espera()
p1.exibir_resumo()