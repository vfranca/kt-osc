import sys


a = float(sys.argv[2])
b = float(sys.argv[1])


def var(a, b):
    "Calcula a variação percentual de b em a." ""
    var_absoluta = a - b
    var_percentual = var_absoluta / a * 100
    return "%.1f%%" % var_percentual


if __name__ == "__main__":
    print(var(a, b))
