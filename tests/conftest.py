import os
import sys
from typing import Generator, Any

import pytest
import sqlalchemy as sa

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session
from starlette.testclient import TestClient

from app.core.config import settings
from app.db.dev_engine import get_session
from app.main import include_router, app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py

TEST_DATABASE_URL = settings.TEST_DATABASE_URL
test_engine = create_engine(TEST_DATABASE_URL, echo=True)


def create_test_db_and_tables():
    SQLModel.metadata.create_all(test_engine)

def delete_test_db_and_tables():
    SQLModel.metadata.drop_all(test_engine)

def start_test_application():
    _app = FastAPI()
    include_router(_app)
    create_test_db_and_tables()
    return _app


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

delete_test_db_and_tables()
create_test_db_and_tables()


@pytest.fixture()
def session():
    delete_test_db_and_tables()
    create_test_db_and_tables()
    connection = test_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    nested = connection.begin_nested()

    @sa.event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.begin_nested()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(session):
    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session
    yield TestClient(app)
    del app.dependency_overrides[get_session]
