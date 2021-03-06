
import pandas as pd
import xlsxwriter as xls
import numpy as np
from scipy.stats import kurtosis, shapiro, skew, kstest, kurtosistest, skewtest, iqr, stats
import pyexcel as p

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

#todas as funçÕes que são nativas da biblioteca são com o inicio em minusculo, as minhas em maiusculo.

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
    
def Kolmogorov(df):
    #print(kstest(df, 'norm'))
    if kstest(df, 'norm')[1] > 0.05:
        return 1
    else:
        return 0

#funções apenas para o grupo 3   
def KurtosisTest(df):
    if kurtosistest(df)[1] > 0.05:
        return 1
    else:
        return 0

def SkewTest(df):
    if skewtest(df)[1] > 0.05:
        return 1
    else:       
        return 0

worksheet = xls.Workbook('../AnaliseExploratoria/PlanilhaResultado.xlsx')

aba_grupo1 = worksheet.add_worksheet('Grupo 1')
aba_grupo2 = worksheet.add_worksheet('Grupo 2')
aba_grupo3 = worksheet.add_worksheet('Grupo 3')

def inserir_cabecalho(aba, titulo):
    bold = worksheet.add_format({'bold': 1})
    aba.write('A1', titulo, bold)
    aba.write('B1', 'Quantidade de lançamentos', bold)
    aba.write('C1', 'Valor Kurtosis', bold)
    aba.write('D1', 'P-value Kurtosis', bold)
    aba.write('E1', 'Kurtosis', bold)
    aba.write('F1', 'Valor Shapiro', bold)
    aba.write('G1', 'P-value Shapiro', bold)
    aba.write('H1', 'Shapiro', bold)
    aba.write('I1', 'Valor Skewness', bold)
    aba.write('J1', 'P-value Skewness', bold)
    aba.write('K1', 'Skewness', bold)
    aba.write('L1', 'Valor Kolmogorov', bold)
    aba.write('M1', 'P-value Kolmogorov', bold)
    aba.write('N1', 'Kolmogorov', bold)
    aba.write('O1', 'Todos V', bold)
    aba.write('P1', 'Todos F', bold)
    aba.write('Q1', 'Apenas Kurtosis V', bold)
    aba.write('R1', 'Apenas Shapiro V', bold)
    aba.write('S1', 'Apenas Skewness V', bold)
    aba.write('T1', 'Apenas Kolmogorov V', bold)
    aba.write('U1', 'Kurtosis e Shapiro V', bold)
    aba.write('V1', 'Kurtosis e Skewness V', bold)
    aba.write('W1', 'Shapiro e Skewness V', bold)
    aba.write('X1', 'Kurtosis e Kolmogorov V', bold)
    aba.write('Y1', 'Skewness e Kolmogorov V', bold)
    aba.write('Z1', 'Shapiro e Kolmogorov V', bold)
    aba.write('AA1', 'Valor Máximo', bold)
    aba.write('AB1', 'Média', bold)
    aba.write('AC1', 'Desvio padrão', bold)
    aba.write('AD1', 'Alpha', bold)
    aba.write('AE1', 'Limite Gama', bold)
    aba.write('AF1', 'Normal | Empate', bold)
    aba.write('AG1', 'Distância interquartil', bold)
    aba.write('AH1', 'Limite Beta', bold)

inserir_cabecalho(aba_grupo1, "Lançamentos de todas as empresas de 6 a 10")
inserir_cabecalho(aba_grupo2, "Lançamentos de todas as empresas de 11 a 20")
inserir_cabecalho(aba_grupo3, "Lançamentos de todas as empresas acima de 21")

def tabela_verdade(aba_grupo, num_linhas, KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar):
    #todos verdadeiros
    if (KurtosisVar == 1 and ShapiroVar == 1 and SkewnessVar == 1 and KolmogorovVar == 1) :
        aba_grupo.write('O' + str(num_linhas), 1)
    else:  
        aba_grupo.write('O' + str(num_linhas), 0)

    #todos falsos
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 0 and KolmogorovVar == 0) :
        aba_grupo.write('P' + str(num_linhas), 1)
    else:  
        aba_grupo.write('P' + str(num_linhas), 0)

    #Apenas Kurtosis Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 0 and SkewnessVar == 0) :
        aba_grupo.write('Q' + str(num_linhas), 1)
    else:  
        aba_grupo.write('Q' + str(num_linhas), 0)

    #Apenas Shapiro Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 1 and SkewnessVar == 0) :
        aba_grupo.write('R' + str(num_linhas), 1)
    else:  
        aba_grupo.write('R' + str(num_linhas), 0)

    #Apenas Skewness Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 1) :
        aba_grupo.write('S' + str(num_linhas), 1)
    else:  
        aba_grupo.write('S' + str(num_linhas), 0)
    
    #Apenas Kolmogorov Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 0 and KolmogorovVar == 1):
        aba_grupo.write('T' + str(num_linhas), 1)
    else:
        aba_grupo.write('T' + str(num_linhas), 0)
        
    #Apenas Kurtosis e Shapiro Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 1 and SkewnessVar == 0) :
        aba_grupo.write('U' + str(num_linhas), 1)
    else:  
        aba_grupo.write('U' + str(num_linhas), 0)

    #Apenas Kurtosis e Skewness Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 0 and SkewnessVar == 1) :
        aba_grupo.write('V' + str(num_linhas), 1)
    else:  
        aba_grupo.write('V' + str(num_linhas), 0)

    #Apenas shapiro e Skewness Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 1 and SkewnessVar == 1) :
        aba_grupo.write('W' + str(num_linhas), 1)
    else:  
        aba_grupo.write('W' + str(num_linhas), 0)
        
    #Apenas Kurtosis e Kolmogorov Verdadeiro
    if (KurtosisVar == 1 and ShapiroVar == 0 and SkewnessVar == 0 and KolmogorovVar == 1) :
        aba_grupo.write('X' + str(num_linhas), 1)
    else:  
        aba_grupo.write('X' + str(num_linhas), 0)
    
    #Apenas Skewness e Kolmogorov Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 0 and SkewnessVar == 1 and KolmogorovVar == 1) :
        aba_grupo.write('Y' + str(num_linhas), 1)
    else:  
        aba_grupo.write('Y' + str(num_linhas), 0)
        
    #Apenas Shapiro e Kolmogorov Verdadeiro
    if (KurtosisVar == 0 and ShapiroVar == 1 and SkewnessVar == 0 and KolmogorovVar == 1) :
        aba_grupo.write('Z' + str(num_linhas), 1)
    else:  
        aba_grupo.write('Z' + str(num_linhas), 0)
    

def normal_empate(aba_grupo, num_linhas, array_testes):
    count = 0
    
    for teste in array_testes:
        if teste == 1:
            count += 1
    
    if count >= 3: 
        aba_grupo.write('AF' + str(num_linhas), 'Normal')
    elif count == 2:
        aba_grupo.write('AF' + str(num_linhas), 'Empate')
    else:
        aba_grupo.write('AF' + str(num_linhas), 'Não atende')

def set_values(values, aba_grupo, num_linhas_1, num_col_1):
    for value in values:
        aba_grupo.write(num_linhas_1, num_col_1, str(value))
        num_col_1 += 1

def funcao(aba, num_linhas, num_col, df, categoria):
    KurtosisVar = Kurtosis(df.Value)
    ShapiroVar = Shapiro(df.Value)
    SkewnessVar = Skewness(df.Value)
    KolmogorovVar = Kolmogorov(df.Value)

    aba.write('A' + str(num_linhas), categoria + ' - ' + key)
    aba.write('B' + str(num_linhas), len(df))

    #valor Kurtosis
    aba.write('C' + str(num_linhas), kurtosis(df.Value))
    aba.write('D' + str(num_linhas), ' - ')
    aba.write('E' + str(num_linhas), KurtosisVar)

    #valor shapiro
    aba.write('F' + str(num_linhas), shapiro((df.Value))[0])
    #p-value shapiro
    aba.write('G' + str(num_linhas), shapiro((df.Value))[1])
    aba.write('H' + str(num_linhas), ShapiroVar)

    #valor skewness
    aba.write('I' + str(num_linhas), skew(df.Value))
    aba.write('J' + str(num_linhas), ' - ')
    aba.write('K' + str(num_linhas), SkewnessVar)

    #valor Kolmogorov
    aba.write('L' + str(num_linhas), kstest((df.Value), 'norm')[0])
    #p-valor Kolmogorov
    aba.write('M' + str(num_linhas), kstest((df.Value), 'norm')[1])
    aba.write('N' + str(num_linhas), KolmogorovVar)

    aba.write('AA' + str(num_linhas), (df.Value).max())

    #média
    aba.write('AB' + str(num_linhas), (df.Value).mean())
    #desvio padrão
    aba.write('AC' + str(num_linhas), (df.Value).std())

    #Alpha 
    aba.write('AD' + str(num_linhas),((((df.Value).max()) - ((df.Value).min()))/((df.Value).mean())))

    #LIMIT_GAMA=3DESVIO_PAD + MEDIA
    aba.write('AE' + str(num_linhas), (3*((df.Value).std())+((df.Value).mean())))

    #Distância interquartil
    aba.write('AG' + str(num_linhas), iqr(df.Value))

    #Limite_beta = Q3 + 2(dist_interquartil)
    aba.write('AH' + str(num_linhas), ((stats.scoreatpercentile((df.Value),75)) + 2*(iqr(df.Value))))

    #Pegar Value e mostrar horizontalmente
    #inicia na linha 0 coluna 35
    set_values(df.Value, aba, num_linhas - 1, num_col)


    tabela_verdade(aba, num_linhas, KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar)    
    normal_empate(aba, num_linhas, [KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar])

    num_linhas += 1

num_col = 35
num_linhas_1 = 2
num_linhas_2 = 2
num_linhas_3 = 2

for key, df in dfs.items():
    for categoria in df.Categoria.unique():
        if((len(df[df.Categoria == categoria]) >= 6) and (len(df[df.Categoria == categoria]) <= 10)):
            #funcao(aba_grupo1, num_linhas_1, num_col, df[df.Categoria == categoria], categoria)
            KurtosisVar = Kurtosis(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = Skewness(df[df.Categoria == categoria].Value)
            KolmogorovVar = Kolmogorov(df[df.Categoria == categoria].Value)
            
            aba_grupo1.write('A' + str(num_linhas_1), categoria + ' - ' + key)
            aba_grupo1.write('B' + str(num_linhas_1), len(df[df.Categoria == categoria]))
                     
            #valor Kurtosis
            aba_grupo1.write('C' + str(num_linhas_1), kurtosis(df[df.Categoria == categoria].Value))
            aba_grupo1.write('D' + str(num_linhas_1), ' - ')
            aba_grupo1.write('E' + str(num_linhas_1), KurtosisVar)
            
            #valor shapiro
            aba_grupo1.write('F' + str(num_linhas_1), shapiro((df[df.Categoria == categoria].Value))[0])
            #p-value shapiro
            aba_grupo1.write('G' + str(num_linhas_1), shapiro((df[df.Categoria == categoria].Value))[1])
            aba_grupo1.write('H' + str(num_linhas_1), ShapiroVar)
            
            #valor skewness
            aba_grupo1.write('I' + str(num_linhas_1), skew(df[df.Categoria == categoria].Value))
            aba_grupo1.write('J' + str(num_linhas_1), ' - ')
            aba_grupo1.write('K' + str(num_linhas_1), SkewnessVar)
            
            #valor Kolmogorov
            aba_grupo1.write('L' + str(num_linhas_1), kstest((df[df.Categoria == categoria].Value), 'norm')[0])
            #p-valor Kolmogorov
            aba_grupo1.write('M' + str(num_linhas_1), kstest((df[df.Categoria == categoria].Value), 'norm')[1])
            aba_grupo1.write('N' + str(num_linhas_1), KolmogorovVar)
            
            aba_grupo1.write('AA' + str(num_linhas_1), (df[df.Categoria == categoria].Value).max())
           
            #média
            aba_grupo1.write('AB' + str(num_linhas_1), (df[df.Categoria == categoria].Value).mean())
            #desvio padrão
            aba_grupo1.write('AC' + str(num_linhas_1), (df[df.Categoria == categoria].Value).std())
          
            #Alpha 
            aba_grupo1.write('AD' + str(num_linhas_1),((((df[df.Categoria == categoria].Value).max()) - ((df[df.Categoria == categoria].Value).min()))/((df[df.Categoria == categoria].Value).mean())))

            #LIMIT_GAMA=3DESVIO_PAD + MEDIA
            aba_grupo1.write('AE' + str(num_linhas_1), (3*((df[df.Categoria == categoria].Value).std())+((df[df.Categoria == categoria].Value).mean())))
            
            #Distância interquartil
            aba_grupo1.write('AG' + str(num_linhas_1), iqr(df[df.Categoria == categoria].Value))
            
            #Limite_beta = Q3 + 2(dist_interquartil)
            aba_grupo1.write('AH' + str(num_linhas_1), ((stats.scoreatpercentile((df[df.Categoria == categoria].Value),75)) + 2*(iqr(df[df.Categoria == categoria].Value))))
            
            #Pegar Value e mostrar horizontalmente
            #inicia na linha 0 coluna 35
            set_values(df[df.Categoria == categoria].Value, aba_grupo1, num_linhas_1 - 1, num_col)
            
            tabela_verdade(aba_grupo1, num_linhas_1, KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar)    
            normal_empate(aba_grupo1, num_linhas_1, [KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar])
            
            num_linhas_1 += 1
            
        elif((len(df[df.Categoria == categoria]) >= 11) and (len(df[df.Categoria == categoria]) <= 20)):
            
            KurtosisVar = Kurtosis(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = Skewness(df[df.Categoria == categoria].Value)
            KolmogorovVar = Kolmogorov(df[df.Categoria == categoria].Value)
            
            aba_grupo2.write('A' + str(num_linhas_2), categoria + ' - ' + key)
            aba_grupo2.write('B' + str(num_linhas_2), len(df[df.Categoria == categoria]))
            
            #valor Kurtosis
            aba_grupo2.write('C' + str(num_linhas_2), kurtosis(df[df.Categoria == categoria].Value))
            aba_grupo2.write('D' + str(num_linhas_2), ' - ')
            aba_grupo2.write('E' + str(num_linhas_2), KurtosisVar)
            
            #valor shapiro
            aba_grupo2.write('F' + str(num_linhas_2), shapiro((df[df.Categoria == categoria].Value))[0])
            #p-value shapiro
            aba_grupo2.write('G' + str(num_linhas_2), shapiro((df[df.Categoria == categoria].Value))[1])
            aba_grupo2.write('H' + str(num_linhas_2), ShapiroVar)
            
            #valor skewness
            aba_grupo2.write('I' + str(num_linhas_2), skew(df[df.Categoria == categoria].Value))
            aba_grupo2.write('J' + str(num_linhas_2), ' - ')
            aba_grupo2.write('K' + str(num_linhas_2), SkewnessVar)
            
            #valor Kolmogorov
            aba_grupo2.write('L' + str(num_linhas_2), kstest((df[df.Categoria == categoria].Value), 'norm')[0])
            #p-valor Kolmogorov
            aba_grupo2.write('M' + str(num_linhas_2), kstest((df[df.Categoria == categoria].Value), 'norm')[1])
            aba_grupo2.write('N' + str(num_linhas_2), KolmogorovVar)
            
            aba_grupo2.write('AA' + str(num_linhas_2), (df[df.Categoria == categoria].Value).max())
           
            #media
            aba_grupo2.write('AB' + str(num_linhas_2), (df[df.Categoria == categoria].Value).mean())
            #desvio padrão
            aba_grupo2.write('AC' + str(num_linhas_2), (df[df.Categoria == categoria].Value).std())
            
            #Alpha 
            aba_grupo2.write('AD' + str(num_linhas_2),((((df[df.Categoria == categoria].Value).max()) - ((df[df.Categoria == categoria].Value).min()))/((df[df.Categoria == categoria].Value).mean())))

            #LIMIT_GAMA
            aba_grupo2.write('AE' + str(num_linhas_2), (3*((df[df.Categoria == categoria].Value).std())+((df[df.Categoria == categoria].Value).mean())))
            
            #Distância interquartil
            aba_grupo2.write('AG' + str(num_linhas_2), iqr(df[df.Categoria == categoria].Value))
            
            #Limite_beta = Q3 + 2(dist_interquartil)
            aba_grupo2.write('AH' + str(num_linhas_2), ((stats.scoreatpercentile((df[df.Categoria == categoria].Value),75)) + 2*(iqr(df[df.Categoria == categoria].Value))))
            
            #Pegar Value e mostrar horizontalmente
            #inicia na linha 0 coluna 35
            set_values(df[df.Categoria == categoria].Value, aba_grupo2, num_linhas_2 - 1, num_col)
            
            tabela_verdade(aba_grupo2, num_linhas_2, KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar)    
            normal_empate(aba_grupo2, num_linhas_2, [KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar])
            
            num_linhas_2 += 1
            
        elif((len(df[df.Categoria == categoria]) >= 21)):
            
            KurtosisVar = KurtosisTest(df[df.Categoria == categoria].Value)
            ShapiroVar = Shapiro(df[df.Categoria == categoria].Value)
            SkewnessVar = SkewTest(df[df.Categoria == categoria].Value)
            KolmogorovVar = Kolmogorov(df[df.Categoria == categoria].Value)
            
            aba_grupo3.write('A' + str(num_linhas_3), categoria + ' - ' + key)
            aba_grupo3.write('B' + str(num_linhas_3), len(df[df.Categoria == categoria]))
            
            #valor Kurtosis
            aba_grupo3.write('C' + str(num_linhas_3), kurtosistest(df[df.Categoria == categoria].Value)[0])
            aba_grupo3.write('D' + str(num_linhas_3), kurtosistest(df[df.Categoria == categoria].Value)[1])
            aba_grupo3.write('E' + str(num_linhas_3), KurtosisVar)
            
            #valor shapiro
            aba_grupo3.write('F' + str(num_linhas_3), shapiro((df[df.Categoria == categoria].Value))[0])
            #p-value shapiro
            aba_grupo3.write('G' + str(num_linhas_3), shapiro((df[df.Categoria == categoria].Value))[1])
            aba_grupo3.write('H' + str(num_linhas_3), ShapiroVar)
            
            #valor skewness
            aba_grupo3.write('I' + str(num_linhas_3), skewtest(df[df.Categoria == categoria].Value)[0])
            aba_grupo3.write('J' + str(num_linhas_3), skewtest(df[df.Categoria == categoria].Value)[1])
            aba_grupo3.write('K' + str(num_linhas_3), SkewnessVar)
            
            #valor Kolmogorov
            aba_grupo3.write('L' + str(num_linhas_3), kstest((df[df.Categoria == categoria].Value), 'norm')[0])
            #p-valor Kolmogorov
            aba_grupo3.write('M' + str(num_linhas_3), kstest((df[df.Categoria == categoria].Value), 'norm')[1])
            aba_grupo3.write('N' + str(num_linhas_3), KolmogorovVar)
            
            aba_grupo3.write('AA' + str(num_linhas_3), (df[df.Categoria == categoria].Value).max())
            
            #média
            aba_grupo3.write('AB' + str(num_linhas_3), (df[df.Categoria == categoria].Value).mean())
            #dedvio padrão
            aba_grupo3.write('AC' + str(num_linhas_3), (df[df.Categoria == categoria].Value).std())
            
            #Alpha 
            aba_grupo3.write('AD' + str(num_linhas_3),((((df[df.Categoria == categoria].Value).max()) - ((df[df.Categoria == categoria].Value).min()))/((df[df.Categoria == categoria].Value).mean())))

            #LIMIT_GAMA
            aba_grupo3.write('AE' + str(num_linhas_3), (3*((df[df.Categoria == categoria].Value).std())+((df[df.Categoria == categoria].Value).mean())))
            
            #Distância interquartil
            aba_grupo3.write('AG' + str(num_linhas_3), iqr(df[df.Categoria == categoria].Value))
            
            #Limite_beta = Q3 + 2(dist_interquartil)
            aba_grupo3.write('AH' + str(num_linhas_3), ((stats.scoreatpercentile((df[df.Categoria == categoria].Value),75)) + 2*(iqr(df[df.Categoria == categoria].Value))))
            
            #Pegar Value e mostrar horizontalmente
            #inicia na linha 0 coluna 35
            set_values(df[df.Categoria == categoria].Value, aba_grupo3, num_linhas_3 - 1, num_col)
            
            tabela_verdade(aba_grupo3, num_linhas_3, KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar)    
            normal_empate(aba_grupo3, num_linhas_3, [KurtosisVar, ShapiroVar, SkewnessVar, KolmogorovVar])
            
            num_linhas_3 += 1

worksheet.close()

