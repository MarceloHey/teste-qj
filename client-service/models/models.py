from sqlalchemy import Integer, String, Date, DateTime, func, Column
from config import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    date = Column(Date(), nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return f"<User {self.name}>"
