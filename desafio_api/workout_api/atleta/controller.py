from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.categorias.models import CategoriaModel
from workout_api.atleta.schema import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.contrib.dependencies import DatabaseDependency

atleta_router = APIRouter()

@atleta_router.post(path="/", summary="Cria um novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)

async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    nome_categoria = atleta_in.categoria.nome
    nome_ct = atleta_in.ct.nome

    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=nome_categoria))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Categoria {nome_categoria} não encontrada.")
    
    ct = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=nome_ct))).scalars().first()

    if not ct:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{nome_ct} não encontrado.")

    try:
        atleta_out = AtletaOut(id=uuid4(), criado_em=datetime.now(timezone.utc).replace(tzinfo=None), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={"categoria", "ct"}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.ct_id = ct.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao criar atleta.")

    return atleta_out

@atleta_router.get(path="/", summary="Retorna todos os atletas", status_code=status.HTTP_200_OK, response_model=list[AtletaOut])

async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaModel] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return [AtletaOut.model_validate(atleta) for atleta in atletas]

@atleta_router.get(path="/{id}", summary="Retorna um atleta pelo id", status_code=status.HTTP_200_OK, response_model=AtletaOut)

async def query(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: list[AtletaModel] = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrado com o id: {id}")

    return AtletaOut.model_validate(atleta)

@atleta_router.patch(path="/{id}", summary="Editar um atleta pelo id", status_code=status.HTTP_200_OK, response_model=AtletaOut)

async def query(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: list[AtletaModel] = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrado com o id: {id}")
    
    atleta_update = atleta_up.model_dump()
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta

@atleta_router.delete(path="/{id}", summary="Deleta um atleta pelo id", status_code=status.HTTP_204_NO_CONTENT)

async def query(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: list[AtletaModel] = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrado com o id: {id}")

    await db_session.delete(atleta)
    await db_session.commit()