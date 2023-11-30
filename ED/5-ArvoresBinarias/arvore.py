## Árvore Binária
class No:
  def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
    self.carga = carga
    self.esquerda = esquerda
    self.direita = direita

  def __str__(self):
    return str(self.carga)

RAIZ = "raiz"
class ArvoreBinaria:
  def __init__(self, raiz: 'No'):
    self.raiz = raiz

  def pos_ordem(self, no: 'No' = RAIZ):
    if no == RAIZ:
      no = self.raiz
    if no is None:
      return no
    if no.esquerda:
      self.pos_ordem(no.esquerda)
    if no.direita:
      self.pos_ordem(no.direita)
    print(no, end=" ")

  def em_ordem(self, no: 'No' = RAIZ):
    if no == RAIZ:
      no = self.raiz
    if no is None:
      return no
    if no.esquerda:
      self.em_ordem(no.esquerda)
    print(no, end=" ")
    if no.direita:
      self.em_ordem(no.direita)

  def pre_ordem(self, no: 'No' = RAIZ):
    if no == RAIZ:
      no = self.raiz
    if no == None:
      return no
    print(no, end=" ")
    if no.esquerda:
      self.pre_ordem(no.esquerda)
    if no.direita:
      self.pre_ordem(no.direita)
