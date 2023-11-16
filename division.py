def dividir(a,b):
    if b == 0:
        return "Un valor no puede ser dividido por 0"
    else:
        return a/b


if __name__ == "__main__":
    print(dividir(7,4))