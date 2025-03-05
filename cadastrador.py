"""
    Projeto de cadastramento de funcionário realizado em prol da avaliação bimestral 
    de Programação e desenvolvimento de sistemas II. Integrantes do grupo:
    - Danton Bernardo Oliveira de Souza
    - Luiz Henrique Ribas Edling
    - Felipe Gorgo Kiçula
    - Gabriel Lau Linhar
"""

'''
    Ações ainda para serem feitas:
        - Verificação de CPF
        - Verificação de Email
        - Verificação de dados iguais
'''

#Bibliotecas
import pandas as pd

#Lista de dados específicos
lista_nomes = []
lista_cpf = []
lista_emails = []
lista_tipo_funcionario = []

#Dicionario para armazenamento geral de dados
dicionario_dados = {
    'NOME': lista_nomes,
    'CPF' : lista_cpf,
    'EMAIL' : lista_emails,
    'TIPO' : lista_tipo_funcionario,
}

#Funções
def titulo():
    print('=-=-=-=-=-=-=-=-=-=-=')
    print('\033[;;44mC A D A S T R A D O R\033[m')
    print('=-=-=-=-=-=-=-=-=-=-=')

def erro():
    print('\033[1;30;31m\n\t!ERRO!\033[m')
    print('\033[0;30;41mOpção inválida! Tente novamente!\033[m\n')

def cadastrar_funcionario():
    print('Para cadastrar um novo funcionário, digite as seguintes informações:')
    lista_nomes.append(input('Nome: '))
    lista_cpf.append(input('\nCPF: '))
    lista_emails.append(input('\nEmail: '))
    while True:
        tipo_funcionario = str(input('\nTipo de funcionário:\n[1]Estagiário\n[2]Junior\n[3]Pleno\n[4]Senior\n=> '))
        if (tipo_funcionario in '1234' and len(tipo_funcionario) == 1):
            if (tipo_funcionario == '1'):
                tipo_funcionario = 'Estagiário'
            elif (tipo_funcionario == '2'):
                tipo_funcionario = 'Junior'
            elif (tipo_funcionario == '3'):
                tipo_funcionario = 'Pleno'
            elif (tipo_funcionario == '4'):
                tipo_funcionario = 'Senior'
            lista_tipo_funcionario.append(tipo_funcionario)
            break
        else:
            erro()
    print('\n\n')

def funcionários_cadastrados():
    if (len(lista_nomes) == 0):
        print('\n\033[1;30;44mInfelizmente nenhum funcionário foi cadastrado ainda!\033[m')
    else:
        tabela_funcionarios = pd.DataFrame(dicionario_dados)
        print(tabela_funcionarios)
    print('\n\n')

#Classes
class relatorios:
    #Variavel auxiliadora em loops para executar o break mais facilmente
    break_all = False

    #Função __init__ indicadora dos dados usados para tal ações
    def __init__(self, nome, cpf, email, tipo_funcionario):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tipo_funcionario = tipo_funcionario

    def editar(self):
        print('\n\n')
        for x in range(0, len(lista_nomes)):
            if lista_nomes[x] == self.nome:
                ajudante_nome = self.nome
                ajudante_cpf = self.cpf
                ajudante_email = self.email
                ajudante_tipo_funcionario = self.tipo_funcionario

        while True:
            edit = str(input('O que deseja editar?\n[1]Nome\n[2]CPF\n[3]Email\n[4]Tipo de funcionario\n\n=> '))
            if ((edit not in ('1234')) or (len(edit) != 1)):
                erro()
            else:
                if (edit == '1'):
                    while True:
                        novo = str(input(f"\nO nome atual registrado é {self.nome}. Digite o novo dado a ser computado\n\n=> "))
                        confirm = str(input(f'O novo nome a ser registrado será {novo}. Confirmar ação? [S / N]'))
                        if (confirm == 'S' or confirm == 's'):
                            break_all = True
                            break
                        else:
                            while True:
                                if (confirm == 'N' or confirm == 'n'):
                                    break
                                else:
                                    erro()
                                    break
                elif (edit == '2'):
                    while True:
                        novo = str(input(f"O CPF atual registrado é {self.cpf}. Digite o novo dado a ser computado\n\n=> "))
                        confirm = str(input(f'O novo CPF a ser registrado será {novo}. Confirmar ação? [S / N]'))
                        if (confirm == 'S' or confirm == 's'):
                            break_all = True
                            break
                        else:
                            while True:
                                if (confirm == 'N' or confirm == 'n'):
                                    break
                                else:
                                    erro()
                                    break
                elif (edit == '3'):
                    while True:
                        novo = str(input(f"O Email atual registrado é {self.email}. Digite o novo dado a ser computado\n\n=> "))
                        confirm = str(input(f'O novo Email a ser registrado será {novo}. Confirmar ação? [S / N]'))
                        if (confirm == 'S' or confirm == 's'):
                            break_all = True
                            break
                        else:
                            while True:
                                if (confirm == 'N' or confirm == 'n'):
                                    break
                                else:
                                    erro()
                                    break
                elif (edit == '4'):
                #Fazer o de tipo de funcionario (op 1 = estagiario, 2 = junior e etc)
                    while True:
                        novo = str(input(f'O tipo de funcionario atual do funcionario {self.nome} é {self.tipo_funcionario}.\nPara editar essa opção, siga as opções:\n[1]Estagiário\n[2]Junior\n[3]Pleno\n[4]Senior\n=> '))
                        if ((novo not in '1234') or (len(novo) != 1)):
                            erro()
                        #else:
                            #if (novo == '1'):

    
            if break_all:
                break
                    
#Main code
while True:
    titulo()
    op = str(input('\nO que deseja realizar?\n[1]Cadastrar novo funcionário\n[2]Ver funcionários cadastrados\n[3]Relatório geral\n[4]Editar um cadastro já existente\n[0]Sair\n\n=> '))

    #Verificação de opção válida ou não
    if (op not in '12340' or len(op) != 1):
        erro()
    #Opções
    elif (op == '0'):
        break
    elif (op == '1'):
        cadastrar_funcionario()
    elif (op == '2'):
        print('\n')
        funcionários_cadastrados()
    #elif (op == '3'):
    #elif (op == '4'):
print('\n\n====================================')
print('|\033[1;30;43m Obrigado por usar nosso sistema! \033[m|')
print('====================================')