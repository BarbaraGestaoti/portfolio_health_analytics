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
