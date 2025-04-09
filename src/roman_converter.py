def decimal_to_roman(num):
    #Lista de valoers decimales y sus equivalentes romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    #cadena vacia para ir armando el romano
    roman = ''
    i = 0
    #mientras el numero sea num > 0 , el numero no ha sido convertido completamente 
    while num > 0:
        for _ in range(num // val[i]):
            roman += syms[i]
            num -= val[i]
        i += 1
    return roman


if __name__ == '__main__':
    entrada = input("Ingresá un número del 1 al 3999: ")

    if entrada.isdigit():
        numero = int(entrada)
        if 1 <= numero <= 3999:
            romano = decimal_to_roman(numero)
            print(f"El número {numero} en números romanos es: {romano}")
        else:
            print("Error: El número debe estar entre 1 y 3999.")
    else:
        print("Error: Tenés que ingresar un número entero.")
