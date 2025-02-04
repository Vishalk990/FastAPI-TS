from models.conn_db import query,Session,transactional
from models.models import Users

@query
def get(filters: dict[str,any] , _db: Session = None) -> Users | None:
    record = (_db.query(Users).filter_by(**filters).first())
    
    if record:
        return record
    return None

@transactional
def create(username:str, email: str, full_name:str, password: str, _db: Session = None) -> Users:
    user = Users(username=username,
                email=email,
                full_name=full_name,
                password=password
                )
    _db.add(user)   