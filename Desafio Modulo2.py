from datetime import datetime

import random

nome = input("Digite seu nome: ")
datanascimento = datetime.strptime(input("Digite sua data de nascimento (em DD/MM/YYYY) "),"%d/%m/%Y").date() 
datacadastro =datetime.now()
cartoes = ["R$50,00","R$250,00","R$120,00"]
presente = cartoes[random.randint(0,len(cartoes)-1)]
print(f"Olá {nome}, seu registro foi concluido com sucesso no dia {datacadastro:%d/%m/%Y}.\nParabens, houve um sorteiro e voce ganhou um vale compras no valor de {presente} ")
