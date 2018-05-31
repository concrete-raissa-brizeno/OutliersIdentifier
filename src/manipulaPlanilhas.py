
# coding: utf-8

# In[1]:


import pandas as pd
import xlsxwriter as xls
import numpy as np
from scipy.stats import kurtosis, shapiro, skew, kstest
#import matplotlib.pyplot as plt
#%matplotlib inline


# In[2]:


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


def Kurtosis(df):
    if kurtosis(df, fisher=True) > 0:
        return 1
    else:
        return 0
    
def Shapiro(df):
    # p-value
    if (shapiro(df)[1]) > 0.05:
        return 1
    else:
        return 0
    
    
def Skewness(df):
    if (skew(df) >= -0.5) and (skew(df) <= 0.5):
        return 1
    else:
        return 0
    
    


# ### Manipulando planilhas

# In[5]:


worksheet = xls.Workbook('../AnaliseExploratoria/PlanilhaResultado.xlsx')
aba_grupo1 = worksheet.add_worksheet('Grupo 1')
aba_grupo2 = worksheet.add_worksheet('Grupo 2')
aba_grupo3 = worksheet.add_worksheet('Grupo 3')


# In[6]:


bold = worksheet.add_format({'bold': 1})

aba_grupo1.write('A1', 'Lançamentos de todas as empresas de 6 a 10', bold)
aba_grupo1.write('B1', 'Quantidade de lançamentos', bold)
aba_grupo1.write('C1', 'Kurtosis', bold)
aba_grupo1.write('D1', 'Shapiro', bold)
aba_grupo1.write('E1', 'Skewness', bold)
aba_grupo1.write('F1', 'Todos V', bold)
aba_grupo1.write('G1', 'Todos F', bold)
aba_grupo1.write('H1', 'Apenas Kurtosis V', bold)
aba_grupo1.write('I1', 'Apenas Shapiro V', bold)
aba_grupo1.write('J1', 'Apenas Skewness V', bold)
aba_grupo1.write('K1', 'Kurtosis e Shapiro V', bold)
aba_grupo1.write('L1', 'Kurtosis e Skewness V', bold)
aba_grupo1.write('M1', 'Shapiro e Skewness V', bold)

aba_grupo2.write('A1', 'Lançamentos de todas as empresas de 11 a 20', bold)
aba_grupo2.write('B1', 'Quantidade de lançamentos', bold)
aba_grupo2.write('C1', 'Kurtosis', bold)
aba_grupo2.write('D1', 'Shapiro', bold)
aba_grupo2.write('E1', 'Skewness', bold)
aba_grupo2.write('F1', 'Todos V', bold)
aba_grupo2.write('G1', 'Todos F', bold)
aba_grupo2.write('H1', 'Apenas Kurtosis V', bold)
aba_grupo2.write('I1', 'Apenas Shapiro V', bold)
aba_grupo2.write('J1', 'Apenas Skewness V', bold)
aba_grupo2.write('K1', 'Kurtosis e Shapiro V', bold)
aba_grupo2.write('L1', 'Kurtosis e Shapiro V', bold)
aba_grupo2.write('M1', 'Shapiro e Skewness V', bold)

aba_grupo3.write('A1', 'Lançamentos de todas as empresas acima de 21', bold)
aba_grupo3.write('B1', 'Quantidade de lançamentos', bold)
aba_grupo3.write('C1', 'Kurtosis', bold)
aba_grupo3.write('D1', 'Shapiro', bold)
aba_grupo3.write('E1', 'Skewness', bold)
aba_grupo3.write('F1', 'Todos V', bold)
aba_grupo3.write('G1', 'Todos F', bold)
aba_grupo3.write('H1', 'Apenas Kurtosis V', bold)
aba_grupo3.write('I1', 'Apenas Shapiro V', bold)
aba_grupo3.write('J1', 'Apenas Skewness V', bold)
aba_grupo3.write('K1', 'Kurtosis e Shapiro V', bold)
aba_grupo3.write('L1', 'Kurtosis e Shapiro V', bold)
aba_grupo3.write('M1', 'Shapiro e Skewness V', bold)



# In[7]:


def tabela_verdade(aba_grupo, num_linhas, KurtosisVar, ShapiroVar, SkewnessVar):
    #todos verdadeiros
    if (KurtosisVar == 1 and ShapiroVar == 1 and SkewnessVar == 1) :
        aba_grupo.write('F' + str(num_linhas), 1)
    else:  
        aba_grupo.write('F' + str(num_linhas), 0)

    #todos falsos
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 0) :
        aba_grupo.write('G' + str(num_linhas), 1)
    else:  
        aba_grupo.write('G' + str(num_linhas), 0)

    #Apenas Kurtosis Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 0 and SkewnessVar == 0) :
        aba_grupo.write('H' + str(num_linhas), 1)
    else:  
        aba_grupo.write('H' + str(num_linhas), 0)

    #Apenas Shapiro Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 1 and SkewnessVar == 0) :
        aba_grupo.write('I' + str(num_linhas), 1)
    else:  
        aba_grupo.write('I' + str(num_linhas), 0)

    #Apenas Skewness Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 1) :
        aba_grupo.write('J' + str(num_linhas), 1)
    else:  
        aba_grupo.write('J' + str(num_linhas), 0)

    #Apenas Kurtosis e Shapiro Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 1 and SkewnessVar == 0) :
        aba_grupo.write('K' + str(num_linhas), 1)
    else:  
        aba_grupo.write('K' + str(num_linhas), 0)

    #Apenas Kurtosis e Skewness Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 0 and SkewnessVar == 1) :
        aba_grupo.write('L' + str(num_linhas), 1)
    else:  
        aba_grupo.write('L' + str(num_linhas), 0)

    #Apenas Kurtosis e Skewness Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 1 and SkewnessVar == 1) :
        aba_grupo.write('M' + str(num_linhas), 1)
    else:  
        aba_grupo.write('M' + str(num_linhas), 0)


# In[8]:


num_linhas_1 = 2
num_linhas_2 = 2
num_linhas_3 = 2

for key, df in dfs.items():
    for categoria in df.Categoria.unique():
        if((len(df[df.Categoria == categoria]) >= 6) and (len(df[df.Categoria == categoria]) <= 10)):
            
            KurtosisVar = Kurtosis(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = Skewness(df[df.Categoria == categoria].Value)
            
            aba_grupo1.write('A' + str(num_linhas_1), categoria + ' - ' + key)
            aba_grupo1.write('B' + str(num_linhas_1), len(df[df.Categoria == categoria]))
            aba_grupo1.write('C' + str(num_linhas_1), KurtosisVar)
            aba_grupo1.write('D' + str(num_linhas_1), ShapiroVar)
            aba_grupo1.write('E' + str(num_linhas_1), SkewnessVar)
                
            tabela_verdade(aba_grupo1, num_linhas_1, KurtosisVar, ShapiroVar, SkewnessVar)    
                
            num_linhas_1 += 1
            
        elif((len(df[df.Categoria == categoria]) >= 11) and (len(df[df.Categoria == categoria]) <= 20)):
            
            KurtosisVar = Kurtosis(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = Skewness(df[df.Categoria == categoria].Value)
            
            aba_grupo2.write('A' + str(num_linhas_2), categoria + ' - ' + key)
            aba_grupo2.write('B' + str(num_linhas_2), len(df[df.Categoria == categoria]))
            aba_grupo2.write('C' + str(num_linhas_2), KurtosisVar)
            aba_grupo2.write('D' + str(num_linhas_2), ShapiroVar)
            aba_grupo2.write('E' + str(num_linhas_2), SkewnessVar)
            
            tabela_verdade(aba_grupo2, num_linhas_2, KurtosisVar, ShapiroVar, SkewnessVar)    
                
            num_linhas_2 += 1
            
        elif((len(df[df.Categoria == categoria]) >= 21)):
            
            KurtosisVar = Kurtosis(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = Skewness(df[df.Categoria == categoria].Value)
            
            aba_grupo3.write('A' + str(num_linhas_3), categoria + ' - ' + key)
            aba_grupo3.write('B' + str(num_linhas_3), len(df[df.Categoria == categoria]))
            aba_grupo3.write('C' + str(num_linhas_3), KurtosisVar)
            aba_grupo3.write('D' + str(num_linhas_3), ShapiroVar)
            aba_grupo3.write('E' + str(num_linhas_3), SkewnessVar)
            
            tabela_verdade(aba_grupo3, num_linhas_3, KurtosisVar, ShapiroVar, SkewnessVar)    
            
            num_linhas_3 += 1

worksheet.close()
