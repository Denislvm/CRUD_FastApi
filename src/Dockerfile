FROM python:3.8

WORKDIR /usr/src/

COPY . .

# install dependencies
RUN pip3 install virtualenv

RUN pip install fastapi

RUN pip install pydantic

RUN pip install pytest

RUN pip install psycopg2-binary

RUN pip install sqlalchemy

RUN pip install uvicorn

RUN pip install requests

RUN pip install pydantic[email]

CMD ["uvicorn", "auth_users.app:app", "--host", "0.0.0.0", "--port", "80"]