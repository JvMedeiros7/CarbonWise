"""
MÓDULO: utils/validators.py
RESPONSÁVEIS: Geral (Pessoa 3 / Pessoa 4)

Este módulo contém funções auxiliares de validação de dados para garantir a consistência
do que é inserido no sistema, antes de passar para os controladores.
"""

def limpar_cnpj(cnpj_sujo: str) -> str:
    """
    Remove caracteres especiais de um CNPJ (deixando apenas números).
    
    Exemplo: "12.345.678/0001-90" -> "12345678000190"
    """
    # TODO: Implementar limpeza de string (remover pontos, barras e traço)
    pass


def validar_cnpj_formato(cnpj: str) -> bool:
    """
    Verifica se o CNPJ possui a quantidade de dígitos necessária ou formato válido.
    """
    # TODO: Implementar validação do tamanho ou padrão do CNPJ
    pass
