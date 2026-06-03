class GaleriaAlienigena:
   def __init__(self, nome_galeria, obras):
       self.nome_galeria = nome_galeria
       self.obras = obras

   def adicionar_item(self, nome, valor):
       if nome != "" and valor > 0:
           self.obras.append({
               "nome": nome,
               "raridade": valor
           })

   def listar_itens(self):
       print("Obras:")
       for obra in self.obras:
           print(f"{obra['nome']}, {obra['raridade']}")

   def calcular_total(self):
       total = 0
       for obra in self.obras:
           total = total + obra["raridade"]
       return total

   def encontrar_item_mais_valioso(self):
       if len(self.obras) == 0:
           return 
       mais_rara = self.obras[0]
       for obra in self.obras:
           if obra["raridade"] > mais_rara["raridade"]:
               mais_rara = obra
       return mais_rara

   def classificar_colecao(self):
       total = self.calcular_total()
       if total < 500:
           return "Galeria comum"
       elif total <= 1500:
           return "Galeria rara"
       else:
           return "Galeria intergaláctica"

   def exibir_relatorio(self):
       obra = self.encontrar_item_mais_valioso()
       print(f"Galeria: {self.nome_galeria}")
       print(f"Raridade total: {self.calcular_total()}")
       if obra:
           print(f"Obra mais rara: {obra['nome']} ({obra['raridade']})")
       print(f"Classificação: {self.classificar_colecao()}")


g1 = GaleriaAlienigena("Galeria 1", [])
g1.adicionar_item("Nebulosa", 700)
g1.adicionar_item("Estelar", 900)
g1.listar_itens()
g1.exibir_relatorio()
