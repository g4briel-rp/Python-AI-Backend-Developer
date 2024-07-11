from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schema import CategoriaIn, CategoriaOut
from workout_api.contrib.dependencies import DatabaseDependency

categoria_router = APIRouter()

@categoria_router.post(path="/", summary="Cria uma nova categoria", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)

async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out

@categoria_router.get(path="/", summary="Retorna todas as categorias", status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])

async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaModel] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@categoria_router.get(path="/{id}", summary="Retorna uma categoria pelo id", status_code=status.HTTP_200_OK, response_model=CategoriaOut)

async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: list[CategoriaModel] = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria não encontrada com o id: {id}")

    return categoria