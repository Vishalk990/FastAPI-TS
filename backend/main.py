from fastapi import FastAPI
from contextlib import asynccontextmanager 
from routers import auth
from models import conn_db, models
from Logger.logger import logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Startup...")
    yield
    logger.info("Server is closing")
    
    
app = FastAPI(title="full stack",lifespan=lifespan)
models.Base.metadata.create_all(bind=conn_db.engine)


app.include_router(router=auth.router)

# @app.get("/")
# async def root():
#     return {"message":"Health check"}