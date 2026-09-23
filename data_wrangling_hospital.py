# -*- coding: utf-8 -*-

# Data Wrangling
# %%

#Pacotes que serão utilizados

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %%

#importando o banco de dados

dados_hospital = pd.read_csv('hospital_patients_real_world.csv')
# %%

# Visualizando dados básicos do dataset

pd.set_option('display.max.columns', None)
print(dados_hospital)
# %%

# Apenas o nome das colunas

dados_hospital.columns
# %%

# Visualizando as primeiras 'n' observações

dados_hospital.head(n=10)
# %%

# Visualizando as últimas 'n' observações

dados_hospital.tail(n=10)
# %%

# Obtendo informações detalhadas sobre as variáveis
#objetct = dados de texto
#int ou float = variável numérica
# Category = variável categórica

dados_hospital.info()
# %%
# Renomeando colunas com base em sua posição, pelo seu número de índice

dados_hospital = dados_hospital.rename(columns={
    dados_hospital.columns[0]: 'id_paciente',
    dados_hospital.columns[1]: 'idade'
})
# %%
# Renomeando colunas com base no nome

dados_hospital = dados_hospital.rename(columns={'Gender': 'genero',
                                               'Diagnosis': 'diagnostico',  })
# %%

# Reescrevendo o objeto

dados_hospital.rename(columns={
    'AdmissionDate': 'data_admissao',
    'DischargeDate': 'data_alta',
    'HospitalID': 'id_hospital'
}, inplace=True)

Parte II

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:53:04 2026

@author: gvs-bsbrasil
"""

import pandas as pd
# %%

# verificando valores nulos
nulos = dados_hospital.isnull().sum()
print('valores nulos por coluna:\n', nulos)
# %%
#Criando um novo DataFrame contendo apenas as linhas que possuem pelo menos um valor nulo.

df_nulos = dados_hospital[dados_hospital.isnull().any(axis=1)]
print(f'total de linhas com valores nulos: {len(df_nulos)}')

# %%

#Verificar o total de linhas duplicadas no DataFrame

duplicadas = dados_hospital.duplicated().sum()
print(f"\nTotal de linhas duplicadas: {duplicadas}")

# %%
# selecionando uma linha com base na sua posição
dados_hospital.iloc[0, ]
# %%
# selecionando uma linha com base na sua posição
dados_hospital.iloc[10, ]
# %%
# selecionando uma coluna com base na sua posição

dados_hospital.iloc[ : , 1]

# %%

# selecionando uma coluna com base na sua posição

dados_hospital.iloc[ : , 6]
# %%
# Selecionando linhas por um intervalo específico e todas as colunas
dados_hospital.iloc[2:5, ]
# %%
# Selecionando colunas por um intervalo específico e todas as linhas
dados_hospital.iloc[ : , 2:4]
# %%

# Selecionando linhas e colunas dentro de intervalos específicos

dados_hospital.iloc[1:300, 1:5]
# %%
# Selecionando uma linha e uma coluna específica
dados_hospital.iloc[3,6]
# %%

# Verificando uma dúvida
# Mostra a contagem de ocorrências de cada ID de hospital
contagem_hospitais = dados_hospital['id_hospital'].value_counts()
print(contagem_hospitais)
# %%
# Transforma a contagem num DataFrame organizado
df_pacientes_hospital = dados_hospital['id_hospital'].value_counts().reset_index()
df_pacientes_hospital.columns = ['id_hospital', 'total_pacientes']

print(df_pacientes_hospital)

# %%
# Selecionando uma variável
dados_hospital['diagnostico']
var_diagnostico = dados_hospital['diagnostico']
# %%

# Selecionando uma variável de outra forma

dados_hospital.genero
var_genero = dados_hospital.genero
# %%

# Selecionando quando é mais de uma variável

dados_hospital[['data_admissao', 'data_alta']]
var_datas = dados_hospital[['data_admissao', 'data_alta']]
# %%

# Padronizando nomes dos registros nas linhas

dados_hospital['diagnostico'] = dados_hospital['diagnostico'].str.lower()
print(dados_hospital['diagnostico'].head())

# %%

# Padronizando data de admissao
dados_hospital['data_admissao'] = pd.to_datetime(dados_hospital['data_admissao'])

# %%

# Padronizando data de alta
dados_hospital['data_alta'] = pd.to_datetime(dados_hospital['data_alta'])
# %%
# Calculando tempo de internação em dias
dados_hospital['tempo_internacao_dias'] = (dados_hospital['data_alta'] - dados_hospital['data_admissao']).dt.days
# %%
# Como verifiquei que há registros de contagem de dias de internação em número negativo após cálculo, presumo que a data de admissão e alta esteja trocada, corrigindo, passo a passo
# Verificando as linhas que contém este erro

linhas_com_erro = dados_hospital[dados_hospital['data_alta'] < dados_hospital['data_admissao']]
print(f"Total de registos com data de alta anterior à admissão: {len(linhas_com_erro)}")
print(linhas_com_erro.head())

# %%

# 2. CORREÇÃO: Inverter os valores onde a data de alta é menor que a de admissão
# Guardamos temporariamente a data de admissão
mask = dados_hospital['data_alta']< dados_hospital['data_admissao']
temp_admissao = dados_hospital.loc[mask, 'data_admissao'].copy()

# %%

# Passamos a data de alta para a coluna de admissão e vice-versa
dados_hospital.loc[mask, 'data_admissao'] = dados_hospital.loc[mask, 'data_alta']
dados_hospital.loc[mask, 'data_alta'] = temp_admissao

# %%

# 3. Recalcular a coluna de tempo de internação agora com as datas corrigidas
dados_hospital['tempo_internacao_dias'] = (dados_hospital['data_alta'] - dados_hospital['data_admissao']).dt.days
# %%

