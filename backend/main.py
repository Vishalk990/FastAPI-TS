from fastapi import FastAPI
from contextlib import asynccontextmanager 
from routers import auth,api
from models import conn_db, models
from Logger.logger import logger
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Startup...")
    yield
    logger.info("Server is closing")
    
    
app = FastAPI(title="full stack",lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

models.Base.metadata.create_all(bind=conn_db.engine)


app.include_router(router=auth.router)
app.include_router(router=api.router)

@app.get("/")
async def root():
    return {"message":"Health check"}