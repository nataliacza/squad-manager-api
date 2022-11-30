from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import JSONResponse

from app.db.dev_engine import get_session
from app.db.models.core_models import Member, Dog
from app.schemas.dogs import (DogDetailsReadDto, SaveDogDto)

dog_router = APIRouter()

@dog_router.post(path="/",
                 response_model=DogDetailsReadDto,
                 summary="Add new dog",
                 status_code=201,
                 responses={201: {"description": "Created"},
                            401: {"description": "Unauthorized"},
                            404: {"description": "Not Found"},
                            405: {"description": "Method Not Allowed"}})
async def add_dog(*, dog_details: SaveDogDto, session: Session = Depends(get_session)):

    get_owner = session.get(Member, dog_details.owner_id)

    if get_owner:
        try:
            new_dog = Dog.from_orm(dog_details)
            session.add(new_dog)
            session.commit()
            session.refresh(new_dog)
            return new_dog

        except ValidationError as error:
            return error

    return JSONResponse(status_code=404, content={"description": "Owner Id Not Found"})


@dog_router.get(path="/",
                response_model=List[DogDetailsReadDto],
                summary="Get all dogs",
                status_code=200,
                responses={200: {"description": "Successful operation"},
                           401: {"description": "Unauthorized"},
                           405: {"description": "Method Not Allowed"}})
async def get_all_dogs(session: Session = Depends(get_session)):

    dogs = session.exec(select(Dog)).all()
    return dogs


@dog_router.get(path="/{dog_id}",
                response_model=DogDetailsReadDto,
                summary="Get dog by id",
                status_code=200,
                responses={200: {"description": "Successful operation"},
                           401: {"description": "Unauthorized"},
                           404: {"description": "Not Found"},
                           405: {"description": "Method Not Allowed"}})
async def get_dog_by_id(dog_id: UUID, session: Session = Depends(get_session)):

    get_dog = session.get(Dog, dog_id)

    if get_dog:
        return get_dog

    return JSONResponse(status_code=404, content={"description": "Id Not Found"})


@dog_router.put(path="/{dog_id}",
                response_model=DogDetailsReadDto,
                summary="Update dog details",
                status_code=200,
                responses={200: {"description": "Successful operation"},
                           401: {"description": "Unauthorized"},
                           404: {"description": "Not Found"},
                           405: {"description": "Method Not Allowed"}})
async def update_dog_details(*, dog_id: UUID, update_dog: SaveDogDto,
                             session: Session = Depends(get_session)):

    get_dog = session.get(Dog, dog_id)

    if get_dog:
        get_member = session.get(Member, update_dog.owner_id)
        if get_member:
            try:
                new_data = update_dog.dict()
                for key, value in new_data.items():
                    setattr(get_dog, key, value)
                session.add(get_dog)
                session.commit()
                session.refresh(get_dog)

                return get_dog

            except ValidationError as error:
                return error

        return JSONResponse(status_code=404, content={"description": "Owner Id Not Found"})

    return JSONResponse(status_code=404, content={"description": "Dog Id Not Found"})


@dog_router.delete(path="/{dog_id}",
                   summary="Delete dog",
                   description="On deletion, all assigned exams will be removed.",
                   status_code=204,
                   responses={204: {"description": "No content"},
                              401: {"description": "Unauthorized"},
                              404: {"description": "Not Found"},
                              405: {"description": "Method Not Allowed"}})
async def delete_dog(*, dog_id: UUID, session: Session = Depends(get_session)):

    get_dog = session.get(Dog, dog_id)

    if get_dog:
        session.delete(get_dog)
        session.commit()
        return {}

    return JSONResponse(status_code=404, content={"description": "Id Not Found"})
