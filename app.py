from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from datetime import datetime
import sys
import json
import os

# Importar funciones locales
from astrogematria_core import calcular_astrogematria_completa
from models import AstrogematriaRequest, AstrogematriaResponse, AstrogematriaData, HealthResponse
from config import settings

# Configurar logging
logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="API para cálculos de astrogematría - Convierte palabras en posiciones zodiacales"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint raíz con información básica del servicio"""
    return {
        "service": settings.app_name,
        "version": settings.version,
        "status": "running",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "calcular": "/astrogematria/calcular",
            "remedios": "/astrogematria/remedios"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check del servicio"""
    try:
        # Test básico de las funciones core
        test_result = calcular_astrogematria_completa("test")
        dependencies_ok = test_result is not None
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        dependencies_ok = False
    
    return HealthResponse(
        status="healthy" if dependencies_ok else "unhealthy",
        service=settings.app_name,
        version=settings.version,
        timestamp=datetime.now(),
        python_version=settings.python_version,
        dependencies_ok=dependencies_ok
    )

@app.post("/astrogematria/calcular", response_model=AstrogematriaResponse)
async def calcular_astrogematria(request: AstrogematriaRequest):
    """
    Calcula el valor astrogematrícico de una palabra o frase
    y determina su posición en la rueda zodiacal
    """
    try:
        logger.info(f"Calculando astrogematría para: {request.palabra}")
        
        # Realizar el cálculo
        resultado = calcular_astrogematria_completa(request.palabra)
        
        # Crear objeto de datos
        data = AstrogematriaData(**resultado)
        
        logger.info(f"Cálculo completado: {resultado['posicion_completa']}")
        
        return AstrogematriaResponse(
            success=True,
            data=data.model_dump(),
            cached=False
        )
        
    except ValueError as e:
        logger.warning(f"Error de validación: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error interno: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/astrogematria/remedios")
async def get_remedios():
    """
    Obtiene la lista de remedios homeopáticos por grado y signo zodiacal
    """
    try:
        # Cargar datos desde el archivo JSON
        remedios_file = os.path.join(os.path.dirname(__file__), "remedios_data.json")
        
        if not os.path.exists(remedios_file):
            raise HTTPException(status_code=404, detail="Archivo de remedios no encontrado")
        
        with open(remedios_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        logger.info(f"Remedios cargados: {len(data['remedios'])} registros")
        
        return {
            "success": True,
            "data": data,
            "total": len(data['remedios'])
        }
        
    except Exception as e:
        logger.error(f"Error cargando remedios: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Iniciando {settings.app_name} en puerto {settings.port}")
    uvicorn.run(
        app, 
        host=settings.host, 
        port=settings.port,
        log_level=settings.log_level.lower()
    )
