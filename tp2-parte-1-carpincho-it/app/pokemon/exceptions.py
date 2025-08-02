from fastapi import HTTPException

PokemonNotFound = HTTPException(status_code=404, detail="Pokemon no encontrado")
MovimientoNotFound = HTTPException(status_code=404, detail="Movimiento no encontrado")
EquipoNotFound = HTTPException(status_code=404, detail="Equipo no encontrado")
GeneracionNotFound = HTTPException(status_code=404, detail="Generacion no encontrada")

EquipoExists = HTTPException(
    status_code=409, detail="El nombre de equipo ya fue registrado"
)
InvalidGeneration = HTTPException(status_code=400, detail="La generación no es válida")
InvalidPokemonIntegrate = HTTPException(
    status_code=400, detail="Los datos del integrante no son validos"
)
MaxIntegranteNumber = HTTPException(
    status_code=409, detail="El equipo ya tiene 6 integrantes"
)
InvalidIntegranteGeneracion = HTTPException(
    status_code=409, detail="El integrante no pertenece a la generacion del equipo"
)
