from workout_api.categorias.schema import CategoriaIn
from workout_api.centro_treinamento.schema import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin
from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=70.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    ct: Annotated[CentroTreinamentoAtleta, Field(description="Centro de Treinamento do atleta")]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass 

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(description="Nome do atleta", example="João", max_length=50)]
    idade: Annotated[Optional[int], Field(description="Idade do atleta", example=25)]

class AtletaOutCustom(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="João", max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    ct: Annotated[CentroTreinamentoAtleta, Field(description="Centro de Treinamento do atleta")]