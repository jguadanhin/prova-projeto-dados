import pandas as pd

#Lendo cada uma das abas da Planilha de Base de Dados
compras = pd.read_excel(r'C:\Users\José Roberto\Desktop\database.xlsx', sheet_name='compras')
bandas = pd.read_excel(r'C:\Users\José Roberto\Desktop\database.xlsx', sheet_name='bandas')
ingressos = pd.read_excel(r'C:\Users\José Roberto\Desktop\database.xlsx', sheet_name='ingressos')

#Verificando qual dia houve o maior faturamento
totaldia1 = compras.loc[compras['show'] == 'Terrestrial Chair', 'gastos'].sum()
totaldia2 = compras.loc[compras['show'] == 'Nascent Letter', 'gastos'].sum()
totaldia3 = compras.loc[compras['show'] == 'Symbolic Toy', 'gastos'].sum()
#print(f'Dia 1: R${totaldia1:.2f}\nDia 2: R${totaldia2:.2f}\nDia 3: R${totaldia3:.2f}')

#Filtrando as pessoas que compraram o ingresso "Pista" e status "Concluído"
pistaingressos = ingressos.loc[(ingressos['tipo'] == 'Pista')&(ingressos['status'] == 'Concluido')]

#Transformando nome das pessoas em uma lista
pistaingressosnome = pistaingressos['nome'].to_list()
comprasingressosnome = compras['nome'].to_list()

#Filtrando as pessoas que compraram o ingresso status "Concluído"
ausenciashow = ingressos.loc[ingressos['status'] == 'Concluido']
nomesausencia = ausenciashow['nome'].to_list()

#Encontrando lista de pessoas que não compareceram ao show porém que tiveram a compra como 'Concluido'
#for n in nomesausencia:
    #if n not in comprasingressosnome:
        #print(n)

#Verificando as pessoas que tiveram status "Não concluído" e "Problema de pagamento" porém que foram ao show:
concorrencia = ingressos.loc[(ingressos['status'] == 'Problema no Pagamento')|(ingressos['status'] == 'Nao Concluido')]
concorrencianome = set(concorrencia['nome'].to_list())
#for n in concorrencianome:
    #if n in comprasingressosnome:
        #print(f'{n}', end=',')

#Verificando e criando tabela de quem desistiu da compra com a AT.
desistencia = ingressos.loc[(ingressos['status'] == 'Problema no Pagamento')|(ingressos['status'] == 'Nao Concluido')]
#desistencia.to_excel('desistencia.xlsx')

#Somando os gastos de todas as pessoas que foram ao show e criando um arquivo
compras1 = compras.groupby(['nome']).sum()
#compras1.to_excel('soma.xlsx')

#Criando um dicionário com nome, gastos e shows
listaquestao5 = pd.read_excel(r'C:\Users\José Roberto\Desktop\database.xlsx', sheet_name='desistencia')
listaquestao5dict = listaquestao5.to_dict(orient='index')

#print(listaquestao5dict)

