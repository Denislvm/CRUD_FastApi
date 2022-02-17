from fastapi import APIRouter, Depends, status, Response
from typing import List

from ..models.database import (
    Model,
    UserCreate,
    UserID,
    UserUpdate,
)
from ..services.operations import OperationsService


router = APIRouter(
    prefix='/api',
)


@router.get('GET/user', response_model=List[Model])
def get_all_users(service: OperationsService = Depends()):
    return service.get_list()


@router.post('POST/user')
def create_user(
    operation_data: UserCreate,
    service: OperationsService = Depends(),
):
    service.create(operation_data)


@router.get('/GET/{operation_id}', response_model=UserID)
def get_user(
    user_id: int,
    service: OperationsService = Depends(),
):
    return service.get(user_id)


@router.put('/PUT/{operation_id}', response_model=UserID)
def update_user(
    user_id: int,
    operation_data: UserUpdate,
    service: OperationsService = Depends(),
):
    return service.update(user_id, operation_data)


@router.delete('/DELETE/user/{operation_id}')
def delete_user(user_id: int, service: OperationsService = Depends()):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

