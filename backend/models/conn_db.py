from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
import os
from Logger.logger import logger
from dotenv import load_dotenv

load_dotenv()


DB_URL = os.environ.get("DB_URL")

engine = create_engine(DB_URL)
logger.info(f"Using database: {DB_URL}")

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def query(func):
    def wrapper(*args,**kwargs):
        db_session=SessionLocal()
        result=None
        try:
            response = func(*args,**kwargs,_db=db_session)
            result = response
        except Exception as e:
            raise e
        finally:
            db_session.close()
        return result
    return wrapper


def transactional(func):
    def wrapper(*args,**kwargs):
        db_session = SessionLocal()
        result = None
        
        try:
            response = func(*args,**kwargs,_db=db_session)
            db_session.commit()
            
            if response:
                if type(response) is list:
                    for i in response:
                        db_session.refresh(i)
                else:
                    db_session.refresh(response)
            result = response
        except Exception as ex:
            db_session.rollback()
            raise ex
        finally:
            db_session.close()
        
        return result
    
    return wrapper