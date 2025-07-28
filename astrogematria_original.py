#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Astrogematría
Calcula el valor astrogematrícico de palabras y su posición en la rueda zodiacal
"""

# Diccionario de valores de letras según astrogematría
VALORES_LETRAS = {
    'a': 1, 'b': 2, 'c': 20, 'd': 4, 'e': 5, 'f': 80, 'g': 3, 'h': 8,
    'i': 10, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'ñ': 50,
    'o': 70, 'p': 80, 'q': 100, 'r': 200, 's': 300, 't': 400,
    'u': 6, 'v': 6, 'w': 6, 'x': 60, 'y': 10, 'z': 7
}

# Signos zodiacales con sus rangos de grados
SIGNOS_ZODIACALES = [
    ('Aries', 0, 29),
    ('Tauro', 30, 59),
    ('Géminis', 60, 89),
    ('Cáncer', 90, 119),
    ('Leo', 120, 149),
    ('Virgo', 150, 179),
    ('Libra', 180, 209),
    ('Escorpio', 210, 239),
    ('Sagitario', 240, 269),
    ('Capricornio', 270, 299),
    ('Acuario', 300, 329),
    ('Piscis', 330, 359)
]

def normalizar_texto(texto):
    """
    Normaliza el texto removiendo tildes y espacios, pero manteniendo ñ
    """
    # Mapeo de caracteres acentuados a sus equivalentes sin tilde
    normalizaciones = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'
    }
    
    # Remover espacios y convertir a minúsculas
    texto_limpio = texto.replace(" ", "").lower()
    
    # Aplicar normalizaciones de tildes
    for acentuada, base in normalizaciones.items():
        texto_limpio = texto_limpio.replace(acentuada, base)
    
    return texto_limpio

def calcular_valor_astrogematrico(texto):
    """
    Calcula el valor astrogematrícico total de un texto
    """
    texto_normalizado = normalizar_texto(texto)
    valor_total = 0
    
    for letra in texto_normalizado:
        if letra in VALORES_LETRAS:
            valor_total += VALORES_LETRAS[letra]
        else:
            print(f"Advertencia: La letra '{letra}' no está en el diccionario de valores")
    
    return valor_total, texto_normalizado

def calcular_reduccion_zodiacal(valor_total):
    """
    Calcula la reducción en la rueda zodiacal según las reglas establecidas
    """
    if valor_total <= 360:
        return 360 - valor_total
    else:
        # Encontrar el próximo múltiplo de 360
        multiplo = ((valor_total // 360) + 1) * 360
        return multiplo - valor_total

def determinar_signo_y_grados(reduccion):
    """
    Determina el signo zodiacal y los grados específicos
    """
    for signo, inicio, fin in SIGNOS_ZODIACALES:
        if inicio <= reduccion <= fin:
            grados_en_signo = reduccion - inicio
            return signo, grados_en_signo
    
    # Si no encuentra el signo (no debería pasar)
    return "Error", 0

def mostrar_resultado(palabra_original, texto_procesado, valor_total, reduccion, signo, grados):
    """
    Muestra el resultado completo del cálculo astrogematrícico
    """
    print("\n" + "="*50)
    print("RESULTADO ASTROGEMATRÍCICO")
    print("="*50)
    print(f"Palabra/frase original: {palabra_original}")
    print(f"Texto procesado: {texto_procesado}")
    print(f"Valor astrogematrícico total: {valor_total}")
    print(f"Reducción rueda zodiacal: {reduccion}")
    print(f"Posición en la carta natal: {grados}º de {signo}")
    print("="*50)

def mostrar_detalle_calculo(texto_procesado):
    """
    Muestra el detalle del cálculo letra por letra
    """
    print(f"\nDetalle del cálculo para '{texto_procesado}':")
    total = 0
    detalles = []
    
    for letra in texto_procesado:
        if letra in VALORES_LETRAS:
            valor = VALORES_LETRAS[letra]
            total += valor
            detalles.append(f"{letra}({valor})")
    
    print(" + ".join(detalles) + f" = {total}")
    return total

def main():
    """
    Función principal del programa
    """
    print("🌟 CALCULADORA DE ASTROGEMATRÍA 🌟")
    print("Calcula el valor astrogematrícico y posición zodiacal de palabras")
    print("-" * 60)
    
    while True:
        try:
            # Solicitar entrada al usuario
            entrada = input("\nIngrese una palabra o frase (o 'salir' para terminar): ").strip()
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("¡Gracias por usar la calculadora de astrogematría!")
                break
            
            if not entrada:
                print("Por favor, ingrese una palabra o frase válida.")
                continue
            
            # Calcular valor astrogematrícico
            valor_total, texto_procesado = calcular_valor_astrogematrico(entrada)
            
            if valor_total == 0:
                print("No se pudo calcular el valor. Verifique que la entrada contenga letras válidas.")
                continue
            
            # Mostrar detalle del cálculo
            mostrar_detalle_calculo(texto_procesado)
            
            # Calcular reducción zodiacal
            reduccion = calcular_reduccion_zodiacal(valor_total)
            
            # Determinar signo y grados
            signo, grados = determinar_signo_y_grados(reduccion)
            
            # Mostrar resultado completo
            mostrar_resultado(entrada, texto_procesado, valor_total, reduccion, signo, grados)
            
            # Preguntar si quiere continuar
            continuar = input("\n¿Desea calcular otra palabra? (s/n): ").strip().lower()
            if continuar in ['n', 'no']:
                print("¡Gracias por usar la calculadora de astrogematría!")
                break
                
        except KeyboardInterrupt:
            print("\n\n¡Gracias por usar la calculadora de astrogematría!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
