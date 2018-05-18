# coding: utf-8

# In[3]:

import os
import pandas as pd
import xlsxwriter as xls
#import matplotlib.pyplot as plt
#%matplotlib inline


# In[4]:

dfs = {
    'CadariEngenharia': pd.read_csv('../DadosFonte/cadariengenhariaearquiteturalt0.csv', sep=',', encoding='ISO-8859-1'),
    'CombogoComunicacao': pd.read_csv('../DadosFonte/combogocomunicacao.csv', sep=',', encoding='ISO-8859-1'),
    'DegrauArquitetos': pd.read_csv('../DadosFonte/degrauarquitetosassociados.csv', sep=',', encoding='ISO-8859-1'),
    'EduardoPepato': pd.read_csv('../DadosFonte/eduardopepato.csv', sep=',', encoding='ISO-8859-1'),
    'Espeo': pd.read_csv('../DadosFonte/espeo.csv', sep=',', encoding='ISO-8859-1'),
    'Fast': pd.read_csv('../DadosFonte/fast.csv', sep=',', encoding='ISO-8859-1'),
    'Fisiotrauma': pd.read_csv('../DadosFonte/fisiotrauma.csv', sep=',', encoding='ISO-8859-1'),
    'gestaoNaPratica': pd.read_csv('../DadosFonte/gestaonapratica.csv', sep=',', encoding='ISO-8859-1'),
    'GrupoDamiam': pd.read_csv('../DadosFonte/grupodamiam.csv', sep=',', encoding='ISO-8859-1'),
    'InovaEmpresaJunior': pd.read_csv('../DadosFonte/inovaempresajunior.csv', sep=',', encoding='ISO-8859-1'),
    'LuzEmSolucoes': pd.read_csv('../DadosFonte/luzemssolucoesempresariais.csv', sep=',', encoding='ISO-8859-1'),
    'MarteInovacaoCultural': pd.read_csv('../DadosFonte/marteinovacaocultural.csv', sep=',', encoding='ISO-8859-1'),
    'Mekatronik': pd.read_csv('../DadosFonte/mekatronik.csv', sep=',', encoding='ISO-8859-1'),
    'NorthStarshipping': pd.read_csv('../DadosFonte/northstarshippingservices.csv', sep=',', encoding='ISO-8859-1'),
    'primusconsultoriaempresarial': pd.read_csv('../DadosFonte/primusconsultoriaempresarial.csv', sep=',', encoding='ISO-8859-1'),
    'signo': pd.read_csv('../DadosFonte/signo.csv', sep=',', encoding='ISO-8859-1'),
    'spazioarchidesign': pd.read_csv('../DadosFonte/spazioarchidesign.csv', sep=',', encoding='ISO-8859-1'),
    'tectobrastelecomltda': pd.read_csv('../DadosFonte/tectobrastelecomltda.csv', sep=',', encoding='ISO-8859-1'),
    'tkcconsulting': pd.read_csv('../DadosFonte/tkcconsulting.csv', sep=',', encoding='ISO-8859-1'),
    'wodesign0': pd.read_csv('../DadosFonte/wodesign0.csv', sep=',', encoding='ISO-8859-1')}


# In[5]:
#dfs['Cadari'].head()
# ### Manipulando planilhas
# In[6]:

worksheet = xls.Workbook('../AnaliseExploratoria/PlanilhaResultado.xlsx')
aba_grupo1 = worksheet.add_worksheet('Grupo 1')
aba_grupo2 = worksheet.add_worksheet('Grupo 2')
aba_grupo3 = worksheet.add_worksheet('Grupo 3')

bold = worksheet.add_format({'bold': 1})

aba_grupo1.write('A1', 'Lançamentos de todas as empresas de 6 a 10', bold)
aba_grupo1.write('B1', 'Quantidade de lançamentos', bold)

aba_grupo2.write('A1', 'Lançamentos de todas as empresas de 11 a 20', bold)
aba_grupo2.write('B1', 'Quantidade de lançamentos', bold)

aba_grupo3.write('A1', 'Lançamentos de todas as empresas acima de 21', bold)
aba_grupo3.write('B1', 'Quantidade de lançamentos', bold)

num_linhas_1 = 2
num_linhas_2 = 2
num_linhas_3 = 2

for key, df in dfs.items():
    for categoria in df.Categoria.unique():
        if((len(df[df.Categoria == categoria]) >= 6) and (len(df[df.Categoria == categoria]) <= 10)):
            aba_grupo1.write('A' + str(num_linhas_1), categoria + ' - ' + key)
            aba_grupo1.write('B' + str(num_linhas_1), len(df[df.Categoria == categoria]))
            num_linhas_1 += 1
        elif((len(df[df.Categoria == categoria]) >= 11) and (len(df[df.Categoria == categoria]) <= 20)):
            aba_grupo2.write('A' + str(num_linhas_2), categoria + ' - ' + key)
            aba_grupo2.write('B' + str(num_linhas_2), len(df[df.Categoria == categoria]))
            num_linhas_2 += 1
        elif((len(df[df.Categoria == categoria]) >= 21)):
            aba_grupo3.write('A' + str(num_linhas_3), categoria + ' - ' + key)
            aba_grupo3.write('B' + str(num_linhas_3), len(df[df.Categoria == categoria]))
            num_linhas_3 += 1

# In[7]:

worksheet.close()


# In[8]:
#plt.rcParams['figure.figsize'] = (10,20)
#plt.scatter(dfs['Cadari'].Value, dfs['Cadari'].Categoria)
#plt.figure(figsize=(0.8,0.8))

