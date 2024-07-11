from workout_api.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import UUID4, Field, PositiveFloat

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT King", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua dos Bobos, 0", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", example="João", max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT King", max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do CT")]