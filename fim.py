# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:54:30 2019

@author: Klessia
"""

# Importação do pandas #
import pandas as pd
import numpy as np

# Menu #
def interface():
    """
    Essa função inicia a interação do usuário com o programa e mostra na tela
    menu de opções oferecidas pelo LuPy.    
    - Valores de retorno:
    opcao - opcao escolhida pelo usuario
    """
    opcao= input("Opções:\n 1-Cadastro de novos empreendimentos.\n 2-Consulta de dados do cliente.\n 3-Modificação da situação de empresas cadastradas.\n 4-Sair do programa.\n Digite o número da opção desejada: ")
    opcao= opcao.strip()
    return opcao

# Cadastro de clientes #
def cadastra_cliente(lupy):
    """
    Essa função tem o intuito de fazer o cadastro
    dos cliente da empresa. tendo nome, condicionante,
    data e situacão como requesitos de cadastro e imprime
    uma mensagem confirmando o cadastro.
    - Valores de entrada:
        cliente - nome do cliente a ser cadastrado no dataframe(str)
        condicionante - condionante do cliente que está sendo cadastrado ao dataframe(str)
        data - data de vencimento da condicionante do cliente que está sendo cadastrado ao dataframe(str)
        situação - situação  da condicionante do cliente que está sendo cadastrado ao dataframe(str)
    - Argumento de entrada:
        lupy - é um dataframe
    - Valores de retorno:
        lupy- dataframe que contém informações adicionadas.
    """
    cliente=input("Nome do cliente: ")
    cliente = cliente.strip()
    cliente_M=cliente.lower()
    condicionante=input("Condicionante: ")
    condicionante= condicionante.strip()
    condicionante=condicionante.lower()
    vencimento=input("Data de vencimento:\n(EX: MM/AAAA) ")
    vencimento= vencimento.strip()
    situacao=input("Situação da condicionante: ")
    situacao= situacao.strip()
    situacao=situacao.lower()
    lupy=lupy.append({"CLIENTE":cliente_M,
               "CONDICIONANTE":condicionante,
               "DATA DE VENCIMENTO":vencimento,
               "SITUAÇÃO":situacao},ignore_index=True)
    print("\nCadastro realizado com sucesso!")
    return lupy

# Consulta de dados do cliente #
def consulta_de_dados_do_cliente(lupy,cond,opcao):
    """
    Essa função realiza a busca no banco de dados por data
    ou nome do cliente.
    -  Argumentos de entrada:
        lupy - banco de dados
        cond - variável a ser atualizada para saber se existe ou não cliente
        ou periodo cadastrado na banco de dados.
        opcao - variável que define qual será a função realizada.
    -  Valores de entrada:
        tipo_de_consul - variável onde o usuário define se vai pesquisar no banco de dados 
        por data ou por cliente(int)
        periodo - data desejada para consulta(str)
        nome_c - nome do cliente a ser pesquisado no banco de dados(str)
    -  Valores de retorno:
        lupy - dataframe dataframe que contém as informações dos clientes.
        cond - variável atualizada.      
    """
    lista_client=list()
    lista_data=list()
    for data in lupy["DATA DE VENCIMENTO"]:
        lista_data.append(data)
    for name_c in lupy["CLIENTE"]:
        lista_client.append(name_c)
    tipo_de_consul=input("Opções:\n 1-Consulta por data;\n 2-consulta por nome do cliente.\nDigite o número da opção desejada: ")
    tipo_de_consul=tipo_de_consul.strip()
    if tipo_de_consul== "1":
        periodo=input("Digite o periodo de consulta:\n(EX: MM/AAAA) ")
        periodo= periodo.strip()
        if periodo in lista_data:
            consulta=lupy.loc[lupy['DATA DE VENCIMENTO']==periodo]
            cond="existe"
            print(consulta)
        else:
            cond="não existe"
            print("\nATENÇÃO!!! Periodo não encontrado.")
    if  tipo_de_consul=="2":
        name_c = input("Digite o nome do cliente: ")
        name_c = name_c.strip()
        name_M = name_c.lower() #Trasforma name_c em minúsculo. 
        if name_M in lista_client:
            consulta=lupy.loc[lupy['CLIENTE']== name_M]
            cond="existe"
            print(consulta)
        else:
            cond="não existe"
            print("\nATENÇÂO!!! Cliente não encontrado.")
    elif tipo_de_consul !="2" and tipo_de_consul !="1":
        print("\nATENÇÃO!!! Opção inválida")
        consulta_de_dados_do_cliente(lupy,cond,opcao)
    if opcao == '3':
        modificacao_dos_dados_dos_clientes_cadastrados(lupy,cond,opcao)
    return lupy

# Modificação de dados #
def modificacao_dos_dados_dos_clientes_cadastrados(lupy,cond,opcao):
    """
    Função que tem o objetivo de alterar os dados dos
    clientes e imprime uma mensagem confirmando a alteração da situação.
    -  Valores de entrada:
        nova_dado - nova situação da situação da condicionante(str)
        linha -  numero da linha do dataframe que o usuário deseja modificar(int)
        coluna - nome da coluna do dataframe que o usuário deseja modificar(str)
    - Argumento de entrada:
        lupy - é um dataframe
        cond - variável atualizada na função de consulta.
        opcao - variável que define qual será a função realizada.
    - Valores de retorno:
        lupy - dataframe que contém as informações atualizadas.
    """
    cabecalho=["CLIENTE","CONDICIONANTE","DATA DE VENCIMENTO","SITUAÇÃO"]
    if cond =="existe":
        while True:
            try:
                linha=int(input("Digite o número da linha a qual deseja modificar: "))
                break
            except:
                print("\nATENÇÃO!!! Número de linha inválido.")
        tamanho_dict=len(lupy)
        if linha>=0 and linha<=(tamanho_dict-1):
            while True:
                coluna = input("Digite o nome da coluna a qual deseja modificar:\n ('Use todas as letras em maiúsculo.') ")
                coluna = coluna.strip() # Tira os espaços desnecessários da string
                if coluna in cabecalho:
                    novo_dado=input("Digite o novo dado: ")
                    novo_dado = novo_dado.strip()
                    modificado = lupy.loc[linha,coluna]=novo_dado
                    print("\nDado modificado com sucesso!")
                    break
                else:
                        print("\nATENÇÃO!!! Coluna inexistente.")
        else:
              print("\nATENÇÂO!!! Linha inexistente.")
    return lupy

# Função principal #
def principal(cond):
    """
    A função 'principal' é responsável por gerenciar todo o programa.
    - Argumento de entrada:
        cond: variável atualizada na função de consulta.
    """
    lupy = pd.read_csv(r'lupyff.csv')
    while True:
        opcao = interface()    
        if opcao == "4":
            print("\nPrograma encerrado.")
            export_csv = lupy.to_csv(r'lupyff.csv',index=False, header = True)
            break
        else:
            if opcao == "1":
                lupy=cadastra_cliente(lupy) # lupy é um dataframe a ser implemenatado futuramente.
            elif opcao == "2":
                lupy=consulta_de_dados_do_cliente(lupy,cond,opcao)
            elif opcao == "3":
                print("\nPara modificar, consulte o periodo ou o cliente desejado para a modificação")
                lupy=consulta_de_dados_do_cliente(lupy,cond,opcao)
            else:
                print("\nDigite uma opção válida.")
cond = "inicial"
principal(cond)

#-------------AGRADECIMENTOS-----------------#
# Toda equipe do LuPy agradace pela disponibilidade e ajuda de todos
# os envolvidos para a realização e efetividade do projeto.
# Agradecemos em especial:
# Deus (Pois Deus é pai não padrasto.)
# Monitores
# Jeyson 
# João Paulo ( JP )
# Pet Amb
# Kevin
# Christopher (Pela oportonidade de contado com o mercado de trabalho
# e o desenvolvimento de habilidades profissionais e de convívio
# em equipe.)