from sqlalchemy import NVARCHAR, BigInteger, ForeignKey, String, UniqueConstraint, text
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    username:Mapped[str] = mapped_column(String(255),index=True,unique=True)
    email: Mapped[str] = mapped_column(String(255),index=True,unique=True)
    full_name: Mapped[str] = mapped_column(String(255),default=None)