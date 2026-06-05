# -*- coding: utf-8 -*-
"""
MÓDULO: views/menu_view.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Este módulo é responsável pela interface do menu principal em linha de comando (CLI).
Ele gerencia o fluxo de execução do programa, apresentando opções para o usuário,
capturando as escolhas e delegando para os respectivos controladores e relatórios.
"""

# Importação dos controladores e views desenvolvidos pelos outros membros
from controllers.empresa_controller import (
    cadastrar_empresa,   # Desenvolvido pela Pessoa 3
    registrar_consumo,   # Desenvolvido pela Pessoa 4
    atualizar_frota,     # Desenvolvido pela Pessoa 6
    excluir_empresa      # Desenvolvido pela Pessoa 6
)
from views.relatorio_view import gerar_relatorio  # Desenvolvido pela Pessoa 5


def menu_principal():
    """
    Função da Pessoa 1: Exibe o menu principal no console e gerencia a navegação.
    
    Desafios/Foco Técnico para Pessoa 1:
        1. Criar o loop de execução infinito (while True) para manter o programa rodando.
        2. Estruturar as condicionais (if/elif/else) com base na escolha numérica do usuário.
        3. Fazer o tratamento adequado das entradas e chamar as respectivas funções
           importadas acima.
        4. Oferecer uma opção para sair do programa (quebrando o loop com break).
    """
    # TODO: Pessoa 1 deve desenhar o layout do menu e as condicionais de chamada
    # Estrutura sugerida:
    # while True:
    #     exibir_opcoes_do_menu()
    #     opcao = input("Escolha uma opção: ")
    #     if opcao == "1":
    #         # Lógica para chamar cadastrar_empresa(...)
    #     elif opcao == "2":
    #         # Lógica para chamar registrar_consumo(...)
    #     ...
    #     elif opcao == "0":
    #         break
    
    pass
