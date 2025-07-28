# 🔮 Astrogematría FastAPI - Microservicio de Numerología Zodiacal

Microservicio FastAPI especializado en cálculos de astrogematría que convierte palabras y frases en posiciones zodiacales precisas usando valores numerológicos tradicionales. Forma parte del ecosistema [Astrowellness](https://github.com/AstrologiaMB/homepageastrowellness) proporcionando análisis numerológico-astrológico avanzado.

## 🎯 Características Principales

### ✨ **Cálculos Astrogematrícicos Avanzados**
- **Tabla Tradicional**: Valores numerológicos clásicos para cada letra
- **Normalización Inteligente**: Manejo automático de tildes y caracteres especiales
- **Soporte Multiidioma**: Incluye caracteres únicos como la ñ española
- **Reducción Zodiacal**: Conversión automática a grados y signos zodiacales
- **Precisión Matemática**: Algoritmos optimizados para cálculos exactos

### 🚀 **Tecnología Moderna**
- **FastAPI**: API REST de alta performance con documentación automática
- **Pydantic**: Validación robusta de datos y modelos tipados
- **CORS Configurado**: Integración seamless con frontend React
- **Logging Avanzado**: Sistema de logs configurable para debugging
- **Health Checks**: Monitoreo automático del estado del servicio

### 🔮 **Funcionalidades Únicas**
- **Procesamiento Inteligente**: Ignora espacios, normaliza tildes automáticamente
- **Múltiples Formatos**: Acepta palabras individuales o frases completas
- **Posicionamiento Zodiacal**: Determina signo, grados y posición exacta
- **API RESTful**: Endpoints claros y bien documentados

## 🏗️ Arquitectura del Sistema

```
astrogematria_fastapi/
├── app.py                          # FastAPI application principal
├── astrogematria_core.py           # Motor de cálculo astrogematrícico
├── models.py                       # Modelos Pydantic para requests/responses
├── config.py                       # Configuración del microservicio
├── requirements.txt                # Dependencias Python
├── homeopathic_gematria_csv.txt   # Tabla de valores numerológicos
└── README.md                       # Documentación completa
```

## 📊 Tabla de Valores Astrogematrícicos

| Letra | Valor | Letra | Valor | Letra | Valor | Letra | Valor |
|-------|-------|-------|-------|-------|-------|-------|-------|
| a     | 1     | h     | 8     | ñ     | 50    | u     | 6     |
| b     | 2     | i     | 10    | o     | 70    | v     | 6     |
| c     | 20    | j     | 10    | p     | 80    | w     | 6     |
| d     | 4     | k     | 20    | q     | 100   | x     | 60    |
| e     | 5     | l     | 30    | r     | 200   | y     | 10    |
| f     | 80    | m     | 40    | s     | 300   | z     | 7     |
| g     | 3     | n     | 50    | t     | 400   |       |       |

## 🌟 Signos Zodiacales y Rangos

| Signo       | Rango de Grados | Elemento | Modalidad |
|-------------|-----------------|----------|-----------|
| Aries       | 0° - 29°59'     | Fuego    | Cardinal  |
| Tauro       | 30° - 59°59'    | Tierra   | Fijo      |
| Géminis     | 60° - 89°59'    | Aire     | Mutable   |
| Cáncer      | 90° - 119°59'   | Agua     | Cardinal  |
| Leo         | 120° - 149°59'  | Fuego    | Fijo      |
| Virgo       | 150° - 179°59'  | Tierra   | Mutable   |
| Libra       | 180° - 209°59'  | Aire     | Cardinal  |
| Escorpio    | 210° - 239°59'  | Agua     | Fijo      |
| Sagitario   | 240° - 269°59'  | Fuego    | Mutable   |
| Capricornio | 270° - 299°59'  | Tierra   | Cardinal  |
| Acuario     | 300° - 329°59'  | Aire     | Fijo      |
| Piscis      | 330° - 359°59'  | Agua     | Mutable   |

## 🚀 Inicio Rápido

### 1. **Instalación**
```bash
# Clonar el repositorio
git clone https://github.com/AstrologiaMB/astrogematria_fastapi.git
cd astrogematria_fastapi

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. **Iniciar el Microservicio**
```bash
# Opción 1: Usando Python directamente
python app.py

# Opción 2: Usando Uvicorn
uvicorn app:app --host 0.0.0.0 --port 8003 --reload
```

### 3. **Verificar Funcionamiento**
```bash
# Health check
curl http://localhost:8003/health

# Información del servicio
curl http://localhost:8003/
```

El servicio estará disponible en:
- **API**: http://localhost:8003
- **Documentación**: http://localhost:8003/docs
- **ReDoc**: http://localhost:8003/redoc

## 📚 API Endpoints

### **Cálculo de Astrogematría**
```http
POST /astrogematria/calcular
Content-Type: application/json

{
  "palabra": "Luis Minvielle"
}
```

**Respuesta**:
```json
{
  "success": true,
  "data": {
    "palabra_original": "Luis Minvielle",
    "palabra_procesada": "luisminvielle",
    "valor_total": 532,
    "valor_reducido": 188,
    "grados_zodiacales": 188,
    "signo_zodiacal": "Libra",
    "grados_en_signo": 8,
    "posicion_completa": "8° de Libra",
    "calculo_detallado": "l(30) + u(6) + i(10) + s(300) + m(40) + i(10) + n(50) + v(6) + i(10) + e(5) + l(30) + l(30) + e(5) = 532"
  },
  "cached": false
}
```

### **Endpoints de Monitoreo**
- `GET /` - Información básica del servicio
- `GET /health` - Health check completo con validación de dependencias
- `GET /docs` - Documentación interactiva Swagger
- `GET /redoc` - Documentación alternativa ReDoc

## 🧮 Algoritmo de Cálculo

### **1. Procesamiento de Entrada**
```python
# Ejemplo: "Luis Minvielle"
entrada = "Luis Minvielle"
procesada = "luisminvielle"  # Espacios removidos, minúsculas
```

### **2. Cálculo de Valor Total**
```python
# l(30) + u(6) + i(10) + s(300) + m(40) + i(10) + n(50) + v(6) + i(10) + e(5) + l(30) + l(30) + e(5)
valor_total = 532
```

### **3. Reducción Zodiacal**
```python
# Si valor > 360, encontrar el próximo múltiplo de 360
if valor_total > 360:
    multiplo = ((valor_total // 360) + 1) * 360  # 720
    valor_reducido = multiplo - valor_total      # 720 - 532 = 188
else:
    valor_reducido = 360 - valor_total
```

### **4. Determinación de Signo**
```python
# 188° cae en el rango de Libra (180° - 209°59')
signo = "Libra"
grados_en_signo = 188 - 180 = 8
posicion_final = "8° de Libra"
```

## 🔧 Configuración Técnica

### **Dependencias Principales**
- **Python**: 3.8+
- **FastAPI**: Framework web moderno
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI de alta performance
- **Pydantic-settings**: Gestión de configuración

### **Variables de Entorno**
```env
# Puerto del servidor
PORT=8003

# Host de binding
HOST=0.0.0.0

# Orígenes CORS permitidos
CORS_ORIGINS=["http://localhost:3000"]

# Nivel de logging
LOG_LEVEL=INFO
```

### **Configuración por Defecto**
- **Puerto**: 8003
- **Host**: 0.0.0.0 (todas las interfaces)
- **CORS**: Configurado para localhost:3000
- **Logging**: Nivel INFO

## 🔗 Integración con Ecosistema Astrowellness

### **Frontend React (sidebar-fastapi)**
```typescript
// Llamada desde el frontend
const response = await fetch('http://localhost:8003/astrogematria/calcular', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ palabra: 'Luis Minvielle' })
});

const { data } = await response.json();
console.log(`Resultado: ${data.posicion_completa}`); // "8° de Libra"
```

### **Integración con Otros Microservicios**
- **Puerto 8001**: Carta Natal API
- **Puerto 8002**: Interpretaciones RAG
- **Puerto 8003**: **Astrogematría** (este servicio)
- **Puerto 8004**: Calendario Personal

### **Flujo de Datos**
```
Frontend → Palabra/Frase → Astrogematría API → Cálculo → Posición Zodiacal → Frontend
```

## 🧪 Ejemplos de Uso

### **Ejemplo 1: Palabra Simple**
```bash
curl -X POST http://localhost:8003/astrogematria/calcular \
  -H "Content-Type: application/json" \
  -d '{"palabra": "Luis"}'
```
**Resultado**: `14° de Aries`

### **Ejemplo 2: Frase Completa**
```bash
curl -X POST http://localhost:8003/astrogematria/calcular \
  -H "Content-Type: application/json" \
  -d '{"palabra": "Luis Minvielle"}'
```
**Resultado**: `8° de Libra`

### **Ejemplo 3: Con Tildes**
```bash
curl -X POST http://localhost:8003/astrogematria/calcular \
  -H "Content-Type: application/json" \
  -d '{"palabra": "canción"}'
```
**Resultado**: `19° de Leo` (tilde normalizado automáticamente)

## 📊 Rendimiento y Optimización

### **Métricas Típicas**
- **Tiempo de respuesta**: < 10ms por cálculo
- **Memoria**: ~20MB en funcionamiento
- **CPU**: Mínimo uso, optimizado para cálculos rápidos
- **Concurrencia**: Soporta múltiples requests simultáneos

### **Optimizaciones Implementadas**
- Algoritmos matemáticos eficientes
- Validación rápida de entrada
- Respuestas JSON optimizadas
- Logging configurable para performance

## 🔍 Reglas de Procesamiento

### **1. Normalización de Caracteres**
- **Espacios**: Se ignoran completamente
- **Tildes**: Se remueven automáticamente (ó→o, á→a, é→e, í→i, ú→u)
- **Ñ**: Se mantiene como carácter único con valor 50
- **Mayúsculas**: Se convierten a minúsculas

### **2. Cálculo de Reducción**
- **Si valor ≤ 360**: Reducción = 360 - valor
- **Si valor > 360**: Reducción = (próximo múltiplo de 360) - valor

### **3. Determinación de Signo**
- Cada signo ocupa exactamente 30° de la rueda zodiacal
- Los grados se calculan como: `grados_en_signo = valor_reducido % 30`

## 🔍 Solución de Problemas

### **Error: Puerto 8003 en uso**
```bash
# Liberar puerto
kill $(lsof -ti:8003)
python app.py
```

### **Error: Dependencias faltantes**
```bash
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall
```

### **Error: Carácter no reconocido**
```bash
# Verificar que el carácter esté en la tabla de valores
# El sistema ignora caracteres no reconocidos automáticamente
```

### **Logs y Debugging**
```bash
# Ver logs en tiempo real (si se configuran)
tail -f astrogematria.log

# Verificar health check
curl http://localhost:8003/health
```

## 🧪 Testing y Validación

### **Test Básico**
```python
# Test de la función core
from astrogematria_core import calcular_astrogematria_completa

resultado = calcular_astrogematria_completa("Luis")
print(resultado)  # Debería mostrar 14° de Aries
```

### **Validación de Cálculos**
- Verificación manual con tabla de valores
- Tests unitarios para casos edge
- Validación de normalización de caracteres

## 📚 Documentación Adicional

- **[API Documentation](http://localhost:8003/docs)** - Documentación interactiva Swagger
- **[ReDoc](http://localhost:8003/redoc)** - Documentación alternativa
- **[Health Check](http://localhost:8003/health)** - Estado del servicio
- **[Ecosistema Astrowellness](https://github.com/AstrologiaMB/homepageastrowellness)** - Proyecto principal

## 🤝 Contribución

Este microservicio es parte del ecosistema Astrowellness. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### **Áreas de Contribución**
- Nuevos sistemas de cálculo numerológico
- Optimizaciones de performance
- Soporte para más idiomas y caracteres
- Documentación y ejemplos
- Tests y validaciones

## 📄 Licencia

Este proyecto es parte del ecosistema Astrowellness desarrollado por AstrologiaMB.

## 🔮 Roadmap

- [ ] **Sistemas Alternativos**: Gematría hebrea, caldea, pitagórica
- [ ] **Cache Inteligente**: Redis para cálculos frecuentes
- [ ] **Batch Processing**: Cálculo de múltiples palabras simultáneamente
- [ ] **Análisis Avanzado**: Patrones numerológicos y estadísticas
- [ ] **API Versioning**: Versionado de endpoints
- [ ] **Multi-idioma**: Soporte para alfabetos no latinos
- [ ] **Métricas Avanzadas**: Monitoring y analytics
- [ ] **Interpretaciones**: Integración con significados numerológicos

## 📞 Soporte

Para soporte técnico o preguntas sobre integración:
- **Issues**: GitHub Issues del repositorio
- **Health Check**: Verificar `/health` endpoint
- **Documentación**: Consultar `/docs` para API reference
- **Logs**: Revisar logs del microservicio para errores específicos

---

**🔮 Desarrollado con precisión numerológica por el equipo de AstrologiaMB**

*Microservicio de astrogematría - Versión 1.0.0*
