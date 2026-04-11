from sqlalchemy import Integer, Column, String, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # You never store the real password - you store the hashed version.
    # When a user registers, you hash their password and store the result here.
    # It's a long string like: $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW
    # You can never reverse it back to the original password.
    hashed_password = Column(String, nullable=False)
    # A flag to enable/disable users without deleting them. In real apps when
    # you "delete" a user you usually just set is_active = False - their data
    # stays in the database but they can't log in. This is called soft delete
    is_active = Column(Boolean, default=True)
