from typing import Optional

from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validator_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError['O título deve ter pelo menos 3 palavras']
        
        return value

cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=1, titulo='Algoritmos e Lógica de Programação', aulas=52, horas=66)
]