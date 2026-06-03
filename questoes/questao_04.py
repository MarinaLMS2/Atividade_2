class MochilaDeMissao:
   def __init__(self, agente, equipamentos, capacidade_maxima):
       self.agente = agente
       self.equipamentos = equipamentos
       self.capacidade_maxima = capacidade_maxima

   def adicionar_equipamento(self, equipamento):
       if equipamento != "" and len(self.equipamentos) < self.capacidade_maxima:
           self.equipamentos.append(equipamento)
           print("Equipamento adicionado.")
       else:
           print("Não foi possível adicionar o equipamento.")

   def listar_equipamentos(self):
       print("Equipamentos:")
       for equipamento in self.equipamentos:
           print(equipamento)

   def contar_equipamentos(self):
       return len(self.equipamentos)

   def verificar_espaco(self):
       if len(self.equipamentos) >= self.capacidade_maxima:
           return "Mochila cheia"
       else:
           return "Ainda possui espaço"

   def exibir_relatorio(self):
       print(f"Agente: {self.agente}")
       print(f"Quantidade de equipamentos: {self.contar_equipamentos()}")
       print(f"Capacidade máxima: {self.capacidade_maxima}")
       print(f"Situação: {self.verificar_espaco()}")


m1 = MochilaDeMissao("Agente 1", [], 3)
m1.adicionar_equipamento("Lanterna")
m1.adicionar_equipamento("Mapa")
m1.listar_equipamentos()
m1.exibir_relatorio()

