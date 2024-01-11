class Conta:
   def __init__(self, numero, cpf, nomeTitular, saldo):
       self.numero = numero
       self.cpf = cpf
       self.nomeTitular = nomeTitular
       self.saldo = saldo
   def depositar(self, valor):
       self.saldo += valor
   def sacar(self,valor):
       if self.saldo < valor:
          return False
       else:
          self.saldo -= valor
          return True
   def gerarextrato(self):
        print(f"numero:{self.numero}\n cpf:{self.cpf}\nsaldo:{self.saldo}")
   def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
           contaDestino.depositar(valor)
           self.saldo -= valor
        return("Transferencia Realizada")