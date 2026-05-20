def calcular_juros_compostos(
    valor,
    taxa,
    tempo
):

    taxa_decimal = taxa / 100

    total = valor * (
        (1 + taxa_decimal) ** tempo
    )

    return {
        "montante": round(total, 2),
        "juros": round(total - valor, 2)
    }