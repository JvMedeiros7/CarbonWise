# -*- coding: utf-8 -*-
"""
MÓDULO: database/db.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Este arquivo inicializa a estrutura de dados global (banco de dados em memória)
que será utilizada por todo o sistema para armazenar as informações das empresas
e seus respectivos consumos.
"""

# Estrutura global do banco de dados (Dicionário)
# Exemplo de estrutura que será populada pelas outras funções:
# banco_dados = {
#     "12.345.678/0001-90": {
#         "nome": "Empresa Exemplo Ltda",
#         "frota": 5,  # Número inteiro de veículos (Pessoa 3)
#         "consumos": [  # Lista de consumos inserida pela Pessoa 4
#             {"litros": 150.0, "kwh": 500.0},
#             {"litros": 200.0, "kwh": 450.0}
#         ]
#     }
# }
banco_dados = {}

# O/A Maestro(a) (Pessoa 1) deve garantir que esta variável esteja disponível
# para importação nos demais módulos de controle (controllers) e visualização (views).
