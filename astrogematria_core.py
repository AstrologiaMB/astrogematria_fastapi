#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funciones core de Astrogematría
Extraídas del archivo original para uso en FastAPI
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

def calcular_astrogematria_completa(palabra_original):
    """
    Función principal que calcula toda la astrogematría de una palabra
    Retorna un diccionario con todos los resultados
    """
    try:
        # Calcular valor astrogematrícico
        valor_total, texto_procesado = calcular_valor_astrogematrico(palabra_original)
        
        if valor_total == 0:
            raise ValueError("No se pudo calcular el valor. Verifique que la entrada contenga letras válidas.")
        
        # Calcular reducción zodiacal
        reduccion = calcular_reduccion_zodiacal(valor_total)
        
        # Determinar signo y grados
        signo, grados = determinar_signo_y_grados(reduccion)
        
        # Crear posición completa
        posicion_completa = f"{grados}º de {signo}"
        
        return {
            "palabra_original": palabra_original,
            "palabra_procesada": texto_procesado,
            "valor_astrogematrico": valor_total,
            "reduccion_zodiacal": reduccion,
            "signo": signo,
            "grados": grados,
            "posicion_completa": posicion_completa
        }
        
    except Exception as e:
        raise ValueError(f"Error en el cálculo astrogematrícico: {str(e)}")
