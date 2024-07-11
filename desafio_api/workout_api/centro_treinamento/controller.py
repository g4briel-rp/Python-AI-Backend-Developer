from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schema import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency

ct_router = APIRouter()

@ct_router.post(path="/", summary="Cria uma novo CT", status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)

async def post(db_session: DatabaseDependency, ct_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    ct_out = CentroTreinamentoOut(id=uuid4(), **ct_in.model_dump())
    ct_model = CentroTreinamentoModel(**ct_out.model_dump())

    db_session.add(ct_model)
    await db_session.commit()

    return ct_out

@ct_router.get(path="/", summary="Retorna todos os CTs", status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])

async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    cts: list[CentroTreinamentoModel] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return cts

@ct_router.get(path="/{id}", summary="Retorna um CT pelo id", status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)

async def query(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    ct: list[CentroTreinamentoModel] = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()

    if not ct:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"CT não encontrado com o id: {id}")

    return ct