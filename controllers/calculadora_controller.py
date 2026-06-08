# -*- coding: utf-8 -*-
"""
MÓDULO: controllers/calculadora_controller.py
RESPONSÁVEL: Pessoa 2 (Motor de Cálculo)

Ficará responsável pela regra de negócio matemática de conversão.
O desafio é garantir que a conversão de litros e kWh para toneladas de carbono (tCO2e)
esteja exata e pronta para ser chamada por outras funções (como a de Relatórios da Pessoa 5).
"""
FATORES_EMISSAO = {
    "energia": 0.08,     # kg CO2e por kWh
    "combustivel": 2.68, # kg CO2e por Litro de diesel
    "transporte": 0.3,   # kg CO2e por km rodado
    "residuos": 0.5,     # kg CO2e por kg de lixo
    "agua": 0.00034      # kg CO2e por Litro de água
}


def calcular_co2(kwh_energia: float, litros_combustivel: float, km_transporte: float, kg_residuos: float, litros_agua: float) -> float:
    """
    Realiza o cálculo de emissões de CO2 equivalentes em toneladas.
    
    Parâmetros:
        litros_combustivel (float): Quantidade de litros consumidos.
        kwh_energia (float): Quantidade de energia consumida em kWh.
        
    Retorna:
        float: Total de CO2 emitido em toneladas (tCO2e).
        
    Observações para a Pessoa 2:
        - Pesquise ou utilize os fatores de emissão oficiais (ex: fator de emissão da gasolina/diesel 
          e o fator médio de emissão do grid elétrico brasileiro - SIN).
        - Exemplo fictício de fatores para estruturação (você deve validar/ajustar):
          * Gasolina: ~2.3 kg CO2 por litro
          * Eletricidade: ~0.1 kg CO2 por kWh
          * Lembre-se de converter o resultado final de kg para toneladas (dividir por 1000).
    """
    # TODO: Pessoa 2 deve implementar a fórmula matemática exata aqui
    # Exemplo de rascunho:
    # emissao_litros = litros_combustivel * FATOR_COMBUSTIVEL
    # emissao_kwh = kwh_energia * FATOR_ENERGIA
    # total_toneladas = (emissao_litros + emissao_kwh) / 1000
    
    kg_energia = kwh_energia * FATORES_EMISSAO["energia"]
    kg_combustivel = litros_combustivel * FATORES_EMISSAO["combustivel"]
    kg_transporte = km_transporte * FATORES_EMISSAO["transporte"]
    kg_residuos = kg_residuos * FATORES_EMISSAO["residuos"]
    kg_agua = litros_agua * FATORES_EMISSAO["agua"]

    total_kg = kg_energia + kg_combustivel + kg_transporte + kg_residuos + kg_agua
    total_toneladas = total_kg / 1000

    return total_toneladas

 