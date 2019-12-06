# CRUD USING A TEXT FILE

import sys
import uuid # Criação de ID's
from time import sleep

''' Informações sobre o projeto: '''

__author__ = "Snarloff"
__license__ = "MIT"
__version__ = "1.0.2"
__date__ = "19/11/2019 - 20/11/2019"

class MakeTable:
	def __init__(self):
		super().__init__()

	@property
	def menu(self):
		return input(
			"-=-"*10 + "\n\n" + 
			 "Painel de Controle\n\n" +
			 "1 - Ver pessoas cadastradas\n"
			 "2 - Cadastrar nova Pessoa\n"
			 "3 - Excluir cadastro\n"
			 "4 - Editar pessoa\n"
			 "5 - Sair do Sistema\n\n" +
			"-=-"*10 + "\n\n" + 
			 "Escolha: "
			)

	def len_archives(self):
		return len(open("data/logs.txt", "r").readlines()) 

	def new_user(self, name:str, age:str):
		with open("data/logs.txt", "a+") as file:
			return file.write(str("%s: %s %s\n" %(str(self.len_archives()+1), str(name), str(age))))

	def del_archives(self, num:int):
		archive = open("data/logs.txt", "r").readlines() # Retorna uma lista
		archive.pop(num)
		archive2 = open("data/logs.txt", "wt")
		return archive2.write("".join(map(str, archive)))

	def edit(self, num:int, user:str, age:str):
		archive = open("data/logs.txt", "r").readlines()
		archive[num] = "%s: %s %s\n" %(num+1, user, age)
		archive2 = open("data/logs.txt", "wt")
		return archive2.write("".join(map(str, archive)))		

	def main(self):
		while True:
			response = self.menu
			if response == "1":
				print("\n%s" %(str(open("data/logs.txt", "r").read())) + "-=-"*10)
			elif response == "2":
				print("-=-"*10)
				self.new_user(name=str(input("Nome: ")), age=int(input("Idade: ")))
				print("Usuário(a) cadastrado(a) com sucesso.")
			elif response == "3":
				print("-=-"*10)			
				self.del_archives(num=int(input("Qual pessoa deseja excluir do Sistema:(%s) "%(self.len_archives()))))
				print("Usuário(a) deletado(a) com sucesso.")
			elif response == "4":
				print("-=-"*10)
				self.edit(num=int(input("Qual pessoa deseja editar do Sistema: ")), 
					user=str(input("Digite o novo nome: ")),
					age=str(input("Digite a nova idade: ")))
			elif response == "5":
				exit()
				break

if __name__ == '__main__':
	MakeTable().main()

