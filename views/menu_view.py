"""
MÓDULO: views/menu_view.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Este módulo é responsável pela interface do menu principal em linha de comando (CLI).
Ele gerencia o fluxo de execução do programa, apresentando opções para o usuário,
capturando as escolhas e delegando para os respectivos controladores e relatórios.
"""

from views.relatorio_view import gerar_relatorio  # Desenvolvido pela Pessoa 5

def exibir_opcoes_do_menu():
    print("\n===== MENU - CARBONWISE =====")
    print('1 - Fazer cadastro')
    print('2 - Ver benefícios da aplicação')
    print('3 - Registrar consumo')
    print('4 - Atualizar frota')
    print('5 - Excluir empresa')
    print('0 - PRA SAIR DO PROGRAMA')
    print('--------------------------------')

def beneficiosAplicacao():
    print('- Meça suas Emissões: Calcule automaticamente sua pegada de carbono com base nos dados operacionais da empresa')
    print('- Reduza o impacto: Receba um plano de ação personalizado com estratégias para reduzir emissões e custos')
    print('- Gere relatórios ESG: Relatórios profissionais prontos para investidores, licitações e compliance ambiental\n')
