from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mynotes.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    records = relationship("Record", back_populates="creator",
                           cascade="all, delete",
                           passive_deletes=True
                           )


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    expired_at = Column(Date)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))

    creator = relationship("Author", back_populates="records")




