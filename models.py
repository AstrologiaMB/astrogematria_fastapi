"""
Modelos Pydantic para FastAPI - Astrogematría API
"""
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any
from datetime import datetime
import re

class AstrogematriaRequest(BaseModel):
    """Datos de entrada para calcular astrogematría"""
    palabra: str = Field(..., min_length=1, max_length=200, description="Palabra o frase a calcular")
    
    @validator('palabra')
    def validate_palabra(cls, v):
        if not v.strip():
            raise ValueError('La palabra no puede estar vacía')
        return v.strip()

class AstrogematriaResponse(BaseModel):
    """Respuesta del cálculo astrogematrícico"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    cached: bool = False

class AstrogematriaData(BaseModel):
    """Datos del resultado astrogematrícico"""
    palabra_original: str
    palabra_procesada: str
    valor_astrogematrico: int
    reduccion_zodiacal: int
    signo: str
    grados: int
    posicion_completa: str

class HealthResponse(BaseModel):
    """Respuesta del health check"""
    status: str
    service: str
    version: str
    timestamp: datetime
    python_version: str
    dependencies_ok: bool
