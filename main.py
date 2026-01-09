from datetime import date

class Lançamento:

  def __init__(self, valor, categoria, data, forma_de_pagamento, status):
    self.valor = valor
    self.categoria = categoria
    self.data = data
    self.forma_de_pagamento = forma_de_pagamento
    self.status = status

  @property # Getter para o valor
  def valor(self):
    return self._valor
  
  @valor.setter # Setter para o valor
  def valor(self, novo_valor):
    if novo_valor <= 0:
      raise ValueError("O valor deve ser maior que 0")
    self._valor = float(novo_valor)

  @property # Getter para a data
  def data(self):
    return self._data

  @data.setter # Setter para a data
  def data(self, nova_data):
    if not isinstance(nova_data, date):
      raise TypeError("Data está no formato errado")
    self._data = nova_data

  @property # Getter para a forma_de_pagamento
  def forma_de_pagamento(self):
     return self.forma_de_pagamento
  
  @forma_de_pagamento.setter # Setter para a forma_de_pagamento
  def forma_de_pagamento(self, nova_forma):
      if not isinstance(nova_forma, str):
          raise TypeError("Forma de pagamento deve ser um texto (Ex: Pix, Dinheiro, Boleto, Cartão)")
      self._forma_de_pagamento = nova_forma

      if not nova_forma.strip():
          raise ValueError("Forma de pagamento não pode estar vazia")
      self._forma_de_pagamento= nova_forma

  @property # Getter para o status
  def status(self):
    return self.status
  
  @status.setter # Setter para o status
  def status(self, novo_status):
      status_ajustado = novo_status.upper().strip()
      permitidos = ["PENDENTE", "PAGO"]
      if status_ajustado not in permitidos:
          raise ValueError(f"Status inválido. Escolha entre: {permitidos}")
      self._status = status_ajustado

  def marcar_como_pago(self):
    self.status = "PAGO"

  def marcar_como_pendente(self):
    self.status = "PENDENTE"

  def esta_pago(self):
    return self.status == "PAGO"
  
  def __str__(self):
     return f"{self.data} - {self.categoria.nome} - R$ {self.valor:.2f}"
  
  def __repr__(self):
      return f"Lançamento(valor={self.valor}, categoria={self.categoria.nome}, data={self.data}"
  
  def __eq__(self, other):
     if not isinstance(other, Lançamento):
        return False

     return (self.valor == other.valor and
              self.categoria.nome == other.categoria.nome and
              self.data == other.data)

  def __lt__(self, other):
     return self.data < other.data
  
#CLASSE 
  
class Receita(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)

class Despesa(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)


class Categoria:

  def __init__(self, nome, tipo, limite_mensal=None, descricao=""):
    
    self.nome = nome
    self.tipo = tipo
    self.limite_mensal = limite_mensal
    self.descricao = descricao

  @property # Getter para o nome
  def nome(self):
    return self._nome

  @nome.setter # Setter para o nome
  def nome(self, novo_nome):
    if not novo_nome:
      raise ValueError("O nome da categoria não pode estar vazio")
    self._nome = novo_nome

  @property # Getter para o limite_mensal
  def limite_mensal(self):
    return self._limite_mensal

  @limite_mensal.setter # Setter para o limite_mensal
  def limite_mensal(self, novo_limite):
    if novo_limite is not None and novo_limite < 0:
      raise ValueError ("O limite mensal não pode ser negativo")
    self._limite_mensal = novo_limite


  def __str__(self):
    return self.nome
    

class OrcamentoMensal:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.lancamentos = []

    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self, novo_mes):
        if novo_mes <1 or novo_mes > 12:
            raise ValueError("Mês deve estar entre 1 e 12")
        self._mes = novo_mes

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, novo_ano):
        if novo_ano <1940 or novo_ano > 2100:
            raise ValueError("Ano deve estar entre 1940 e 2100")
        self._ano = novo_ano

    def adicionar_lancamento(self, lancamento):
        self.lancamentos.append(lancamento)
    
    def calcular_total_receitas(self):
        total = 0
        for lancamento in self.lancamentos:
           if isinstance (lancamento, Receita):
               total += lancamento.valor
        return total
    
    def calcular_total_despesas(self):
        total = 0
        for lancamento in self.lancamentos:
           if isinstance (lancamento, Despesa):
               total += lancamento.valor
        return total
    
    def calcular_saldo(self):
       return self.calcular_total_receitas() - self.calcular_total_despesas()
    
    def alerta_saldo_negativo(self):
       saldo_atual = self.calcular_saldo()
       if saldo_atual < 0:
          return "Alerta: Seu saldo está negativo!"
       else:
          return "Saldo está positivo."
       

