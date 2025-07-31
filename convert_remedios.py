#!/usr/bin/env python3
"""
Script para convertir el archivo TXT de remedios homeopáticos a formato JSON
compatible con la API de astrogematría.
"""

import csv
import json
import os

def convert_txt_to_json():
    """Convierte el archivo TXT de remedios a formato JSON"""
    
    # Archivos de entrada y salida
    input_file = 'listado remedio homeopatia por grado y signo.txt'
    output_file = 'remedios_data.json'
    
    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_file):
        print(f"❌ Error: No se encontró el archivo {input_file}")
        return False
    
    remedios = []
    
    try:
        # Leer el archivo CSV
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convertir cada fila a la estructura esperada
                remedio = {
                    "grado": int(row['Grados']),
                    "signo": row['Signo_Zodiacal'],
                    "remedio": row['Sustancia_Homeopatica']
                }
                remedios.append(remedio)
        
        # Crear la estructura JSON final compatible con la API
        data = {
            "success": True,
            "data": {
                "remedios": remedios,
                "total": len(remedios)
            }
        }
        
        # Guardar el archivo JSON
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        
        print(f"✅ Conversión exitosa!")
        print(f"📊 Total de remedios convertidos: {len(remedios)}")
        print(f"📁 Archivo generado: {output_file}")
        
        # Mostrar estadísticas por signo
        signos_stats = {}
        for remedio in remedios:
            signo = remedio['signo']
            if signo not in signos_stats:
                signos_stats[signo] = 0
            signos_stats[signo] += 1
        
        print("\n📈 Estadísticas por signo:")
        for signo, count in sorted(signos_stats.items()):
            print(f"   {signo}: {count} remedios")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante la conversión: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Iniciando conversión de remedios TXT a JSON...")
    success = convert_txt_to_json()
    
    if success:
        print("\n🎉 ¡Conversión completada exitosamente!")
    else:
        print("\n💥 La conversión falló. Revisa los errores arriba.")
