"""
Este es un módulo de ejemplo

Contiene una variable llamada "costo_afinia" y una función llamada "calcular_costo"
"""

costo_afinia = 100

def calcular_costo(consumo, tarifa):
    """
    Calcula el costo de un consumo dado y una tarifa dada

    Parámetros:
    consumo -- consumo en kWh
    tarifa -- tarifa en $/kWh

    Retorna:
    costo -- costo en $
    """
    costo = consumo * tarifa
    return costo