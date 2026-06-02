class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
      self.nome = nome 
      self.destino = destino
      self.energia_necessaria = energia_necessaria
      self.energia_disponivel = energia_disponivel

    def pode_abrir(self):
        if self.energia_necessaria < self.energia_disponivel:
           print(self.calcular_falta_energia())
        else:
           print("portal aberto")
    
    def calcular_falta_energia(self):
        return self.energia_disponivel - self.energia_necessaria
      
    def classificar_estabilidade(self):
        if self.calcular_falta_energia() <= 20:
           print("portal quase estável")
        elif self.calcular_falta_energia() > 20:
            print("portal instável")
        else:
           print("portal estável")

    def exibir_resumo(self):
       print(f"Nome do portal: {self.nome}, Destino: {self.destino}, Energia disponivel: {self.energia_disponivel}, Energia Necessária: {self.energia_necessaria}, situancao do potal: ", self.classificar_estabilidade() )
        
p1 = PortalDimensional("p1","poa", 50, 40) 
p1.pode_abrir()
print(p1.calcular_falta_energia())
p1.classificar_estabilidade()
p1.exibir_resumo()
