# Calcula variação percentual de b em a


def var(preco_final, preco_inicial):
    "Calcula a variação percentual entre dois precos." ""
    var_absoluta = preco_final - preco_inicial
    var_percentual = var_absoluta / preco_inicial * 100
    return "%.1f%%" % var_percentual
