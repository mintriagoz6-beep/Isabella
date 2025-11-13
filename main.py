def multiply(a, b):
    """Devuelve el producto de dos números (soporta int/float)."""
    return a * b

def main():
    try:
        x = float(input("Número 1: "))
        y = float(input("Número 2: "))
    except ValueError:
        print("Entrada no válida. Usa números (p. ej. 3.5 o 2).")
        return
    resultado = multiply(x, y)
    # Muestra sin decimales si ambos eran enteros
    if x.is_integer() and y.is_integer():
        print(f"{int(x)} × {int(y)} = {int(resultado)}")
    else:
        print(f"{x} × {y} = {resultado}")

if __name__ == "__main__":
    main()