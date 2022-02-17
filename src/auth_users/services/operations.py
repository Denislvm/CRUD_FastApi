from .. import tables
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from auth_users.db import get_session
from ..models.database import UserCreate, UserUpdate

from typing import List, Optional


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Tables]:
        take_models = (
            self.session
            .query(tables.Tables).all()
        )
        return take_models

    def create(self, operation_data: UserCreate) -> tables.Tables:
        operation = tables.Tables(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def _get(self, user_id: int) -> Optional[tables.Tables]:
        operation = (
            self.session
                .query(tables.Tables)
                .filter_by(id=user_id
            )
                .first()
        )
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return operation

    def get(self, user_id: int) -> tables.Tables:
        return self._get(user_id)

    def update(self, user_id: int, operation_data: UserUpdate):
        operation = self.get(user_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, user_id: int):
        operation = self.get(user_id)
        self.session.delete(operation)
        self.session.commit()