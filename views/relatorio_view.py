# -*- coding: utf-8 -*-
"""
MÓDULO: views/relatorio_view.py
RESPONSÁVEL: Pessoa 5 (Relatórios - Read)

Este módulo é responsável por exibir os relatórios de emissões das empresas.
É o componente mais visual e focado em apresentação de dados para o usuário.
"""

from database.db import banco_dados
from controllers.calculadora_controller import calcular_co2  # Desenvolvido pela Pessoa 2


def gerar_relatorio(cnpj: str):
    """
    Função da Pessoa 5: Gera e imprime na tela o relatório detalhado de emissões de uma empresa.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa cujo relatório deve ser gerado.
        
    Desafios/Foco Técnico para Pessoa 5:
        1. Tratar erros caso o CNPJ buscado não exista no dicionário (utilizar bloco try-except KeyError).
        2. Obter a lista de consumos da empresa a partir do dicionário 'banco_dados'.
        3. Criar um loop (for) para percorrer o histórico de consumos da empresa.
        4. Dentro do loop, chamar a função 'calcular_co2(litros, kwh)' (Pessoa 2)
           para cada item e acumular/somar o total das emissões.
        5. Exibir os resultados de forma formatada e visualmente limpa (ex: tabelas simples, 
           somatórios e a frota de veículos cadastrada).
    """
    # TODO: Pessoa 5 deve implementar a busca no dict, try-except KeyError, o loop e a exibição
    # Estrutura sugerida:
    # try:
    #     empresa = banco_dados[cnpj]
    #     total_co2 = 0.0
    #     # loop pelos consumos
    #     for consumo in empresa["consumos"]:
    #         total_co2 += calcular_co2(consumo["litros"], consumo["kwh"])
    #     exibir_relatorio_formatado(empresa, total_co2)
    # except KeyError:
    #     exibir_mensagem_de_erro_cnpj_nao_encontrado()
    
    pass
