import uvicorn
import tables
from db import engine

tables.Base.metadata.create_all(bind=engine)

uvicorn.run(
    'auth_users.app:app',
    reload=True,
)