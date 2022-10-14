from typing import List

from fastapi import APIRouter
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import JSONResponse

from app.core.database import engine
from app.models.dogs import Dog
from app.models.members import Member
from app.schemas.dogs import DogDto, CreateDogDto

dogs_router = APIRouter(prefix="/dogs",
                        tags=["Dogs"])


@dogs_router.post(path="/",
                  response_model=DogDto,
                  summary="Add new dog",
                  status_code=201,
                  responses={201: {"detail": "Created"},
                             401: {"detail": "Unauthorized"},
                             404: {"detail": "Not Found"},
                             405: {"detail": "Method Not Allowed"}})
async def add_dog(dog_details: CreateDogDto):

    with Session(engine) as session:
        get_owner = session.get(Member, dog_details.owner_id)

        if get_owner:
            try:
                new_dog = Dog(**dog_details.dict())
                session.add(new_dog)
                session.commit()
                session.refresh(new_dog)
                return new_dog

            except ValidationError as error:
                return error

        return JSONResponse(status_code=404, content={"detail": "Owner Id Not Found"})


@dogs_router.get(path="/",
                 response_model=List[DogDto],
                 summary="Get all dogs",
                 status_code=200,
                 responses={200: {"detail": "Successful operation"},
                            401: {"detail": "Unauthorized"},
                            405: {"detail": "Method Not Allowed"}})
async def get_all_dogs():

    with Session(engine) as session:
        dogs = session.exec(select(Dog)).all()
        return dogs


@dogs_router.get(path="/{id}",
                 response_model=DogDto,
                 summary="Get dog by id",
                 status_code=200,
                 responses={200: {"detail": "Successful operation"},
                            401: {"detail": "Unauthorized"},
                            404: {"detail": "Not Found"},
                            405: {"detail": "Method Not Allowed"}})
async def get_dog_by_id(id: int):

    with Session(engine) as session:
        get_dog = session.get(Dog, id)

        if get_dog:
            return get_dog

        return JSONResponse(status_code=404, content={"detail": "Id Not Found"})
