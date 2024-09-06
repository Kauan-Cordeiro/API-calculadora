from models.dispositivo import DispositivoDB


def calcular_consumo(eletrodomesticos: list[DispositivoDB]):
    consumo_diario = 0
    for dispositivo in eletrodomesticos:
        consumo_diario += dispositivo.consumo * dispositivo.uso_diario

    consumo_mensal = consumo_diario * 30
    consumo_anual = consumo_diario * 365

    return {
        'consumo_diario': consumo_diario,
        'consumo_mensal': consumo_mensal,
        'consumo_anual': consumo_anual
    }